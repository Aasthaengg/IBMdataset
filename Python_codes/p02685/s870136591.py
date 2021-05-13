MOD = 998244353
MAX = int(2e5)


def div(a, b):
    return a * pow(b, MOD-2, MOD) % MOD


FACT = [1] * (MAX+1)
for i in range(1, MAX+1):
    FACT[i] = (i * FACT[i-1]) % MOD
INV = [1] * (MAX+1)
INV[MAX] = div(1, FACT[MAX])
for i in range(MAX, 0, -1):
    INV[i-1] = (INV[i] * i) % MOD


def main():
    N, M, K = map(int, input().split())
    ans = 0
    for i in range(K+1):
        tmp = M * pow(M-1, (N-1-i), MOD) % MOD
        # (N-1)Ci
        tmp = tmp * FACT[N-1] * INV[N-1-i] * INV[i] % MOD
        ans = (ans + tmp) % MOD
    print(ans)


if __name__ == "__main__":
    main()
