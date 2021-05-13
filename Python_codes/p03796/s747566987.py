N = int(input())
MOD = 10 ** 9 + 7
S = 1
for i in range(1, N + 1):
    S = S * i % MOD
print(S % MOD)