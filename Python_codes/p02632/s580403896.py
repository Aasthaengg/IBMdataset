import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = float('inf')
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    _LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())
    SI = lambda : sys.stdin.readline().rstrip()
    DD = ((1,0),(0,1),(-1,0),(0,-1))

    K = NI()
    S = SI()
    LS = len(S)

    f = [1]
    r = [1]
    c = 1
    for i in range(1, K + LS +1):
        c = (c * i) % MOD
        f.append(c)
        r.append(pow(c, MOD - 2, MOD))

    def comb(n, k):
        return (f[n] * r[k] * r[n - k]) % MOD

    ans = 0
    for i in range(K+1):
        ans = (ans + pow(25,i,MOD) * pow(26,K-i,MOD) * comb(i+LS-1,LS-1)) % MOD
    print(ans)

if __name__ == '__main__':
    main()