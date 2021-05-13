s = int(input())
MOD = 10**9 + 7
C = [0]*(s + 1)
C[0] = 1
for n in range(3, s+1): C[n] = (C[n-1] + C[n-3]) % MOD
print(C[s])
