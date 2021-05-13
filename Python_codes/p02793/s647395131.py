def main():
    from math import sqrt
    from fractions import gcd
    from collections import defaultdict
    from copy import deepcopy

    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    p = [1] * (1001)
    P = []  # 1000までの素数表
    p[0] = p[1] = 0
    for x in range(2, int(sqrt(1000000)) + 1):
        if p[x]:
            P.append(x)
            for y in range(x * x, 1001, x):
                p[y] = 0

    B = [defaultdict(int) for i in range(N)]  # N個の数を素因数分解したもの
    lcm = defaultdict(int)  # N個の数のlcmを素因数分解したもの

    for i in range(N):
        for j in P:
            if A[i] % j == 0:
                while A[i] % j == 0:
                    A[i] //= j
                    B[i][j] += 1
            lcm[j] = max(lcm[j], B[i][j])
        if A[i] != 1:
            B[i][A[i]] = 1
            lcm[A[i]] = 1

    l = 1  # N個の数のlcm
    for i in lcm.keys():
        l = (l * pow(i, lcm[i], mod)) % mod

    ans = 0
    # l/A[i]の和を求めていく
    for i in range(N):
        r = l
        for j in list(B[i].keys()):
            r = (r * pow(j, mod - B[i][j] - 1, mod)) % mod
        ans = (ans + r) % mod

    print(ans)

if __name__ == '__main__':
    main()