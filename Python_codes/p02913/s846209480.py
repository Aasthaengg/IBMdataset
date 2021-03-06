import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():


    class SuffixArray:
        """
        construct:
            suffix array: O(N(logN)^2)
            lcp array: O(N)
            sparse table: O(NlogN)
        query:
            get_lcp: O(1)
        """

        def __init__(self, s):
            """
            s: str
            """
            self.__s = s
            self.__n = len(s)
            self.__suffix_array()
            self.__lcp_array()
            self.__sparse_table()

        # suffix array
        def __suffix_array(self):
            s = self.__s
            n = self.__n
            # initialize
            sa = list(range(n))
            rank = [ord(s[i]) for i in range(n)]
            tmp = [0]*n
            k = 1
            def cmp_key(i): return (rank[i], rank[i+k] if i+k < n else -1)
            # iterate
            while(k <= n):
                sa.sort(key=cmp_key)
                tmp[sa[0]] = 0
                for i in range(1, n):
                    tmp[sa[i]] = tmp[sa[i-1]]+(cmp_key(sa[i-1]) < cmp_key(sa[i]))
                rank = tmp[:]
                k <<= 1
            self.__sa = sa
            self.__rank = rank

        # LCP array
        def __lcp_array(self):
            n = self.__n
            s = self.__s
            sa = self.__sa
            rank = self.__rank
            lcp = [0]*n
            h = 0
            for i in range(n):
                j = sa[rank[i]-1]
                if h > 0:
                    h -= 1
                while j+h < n and i+h < n and s[j+h] == s[i+h]:
                    h += 1
                lcp[rank[i]] = h
            self.__lcp = lcp

        # sparse table (LCPのminをとるindexを持つ)
        def __sparse_table(self):
            n = self.__n
            logn = max(0, (n-1).bit_length())
            table = [[0]*n for _ in range(logn)]
            table[0] = list(range(n))
            # construct
            for i in range(1, logn):
                for k in range(n):
                    if k+(1 << (i-1)) >= n:
                        table[i][k] = table[i-1][k]
                        continue
                    if self.__lcp[table[i-1][k]] <= self.__lcp[table[i-1][k+(1 << (i-1))]]:
                        table[i][k] = table[i-1][k]
                    else:
                        table[i][k] = table[i-1][k+(1 << (i-1))]
            self.__table = table

        def get_lcp(self, a, b):
            """
            a,b: int 0<=a,b<n
            return LCP length between s[a:] and s[b:]
            """
            if a == b:
                return self.__n-a
            l, r = self.__rank[a], self.__rank[b]
            l, r = min(l, r)+1, max(l, r)+1
            if r-l == 1:
                return self.__lcp[l]
            i = (r-l-1).bit_length()-1
            if self.__lcp[self.__table[i][l]] <= self.__lcp[self.__table[i][r-(1 << i)]]:
                return self.__lcp[self.__table[i][l]]
            else:
                return self.__lcp[self.__table[i][r-(1 << i)]]
    n = int(input())
    s = input()
    sa = SuffixArray(s)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, min(sa.get_lcp(i, j), j-i))
    print(ans)



resolve()