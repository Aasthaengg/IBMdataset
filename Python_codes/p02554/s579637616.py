MOD = 10 ** 9 + 7
N = int(input())

S_all = pow(10, N, MOD)
S_0 = pow(9, N, MOD)
S_9 = S_0
S_09 = pow(8, N, MOD)

ans = (S_all - (S_0 + S_9 - S_09)) % MOD
print(ans)
