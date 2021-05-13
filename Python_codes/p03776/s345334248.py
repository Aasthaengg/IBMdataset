MOD = 1
m = 100
COMB_table = [[0]*(m+1) for _ in range(m+1)]

fac = [0] * m
finv = [0] * m
inv = [0] * m


def COMBinitialize(m):
    fac[0] = 1
    finv[0] = 1
    if m > 1:
        fac[1] = 1
        finv[1] = 1
        inv[1] = 1
        for i in range(2, m):
            fac[i] = fac[i-1] * i % MOD
            inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
            finv[i] = finv[i - 1] * inv[i] % MOD


def COMB(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


def make_COMB_table(m):
    for i in range(m+1):
        for j in range(i+1):
            if j == 0 or j == i:
                COMB_table[i][j] = 1
            else:
                COMB_table[i][j] = COMB_table[i-1][j-1] + COMB_table[i-1][j]


def COMB_2(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return COMB_table[n][k]


make_COMB_table(m)


def main():
    from collections import Counter
    N, A, B = (int(i) for i in input().split())
    V = [int(i) for i in input().split()]
    V.sort(reverse=True)
    ans = sum(v for v in V[:A])/A
    c = Counter(V)
    c_ans = Counter(V[:A])
    cnt = 0
    if V[0] != V[A-1]:
        cnt = COMB_2(c[V[A-1]], c_ans[V[A-1]])
    else:
        for i in range(A, B+1):
            cnt += COMB_2(c[V[0]], i)
    print(ans)
    print(cnt)


if __name__ == '__main__':
    main()
