N, K = [int(i) for i in input().split(' ')]
MOD = 10 ** 9 + 7

COUNT = {}
for i in range(K,0,-1):
    whole = pow((K//i), N, MOD)

    c = 2
    while i * c <= K:
        whole -= COUNT[i*c]
        c += 1

    COUNT[i] = whole % MOD

SUM = 0
for k, v in COUNT.items():
    SUM += k * v
    SUM %= MOD

print(SUM)
