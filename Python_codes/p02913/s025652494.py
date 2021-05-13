import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def ZAlgorithm(S):
        n = len(S)
        res = [0] * n
        res[0] = n
        i = 1
        j = 0
        while i < n:
            while i + j < n and S[j] == S[i + j]:
                j += 1
            res[i] = j
            if j == 0:
                i += 1
                continue
            k = 1
            while i + k < n and k + res[k] < j:
                res[i + k] = res[k]
                k += 1
            i += k
            j -= k
        return res

    n = int(input())
    S = input()

    res = 0
    for i in range(n):
        T = S[i:]
        LCP = ZAlgorithm(T)
        for j in range(len(T)):
            l = min(LCP[j], j)
            res = max(res, l)
    print(res)


if __name__ == '__main__':
    resolve()
