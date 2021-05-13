mod = 10**9+7
L = input()
dp0 = [0] * (len(L)+1)
dp1 = [0] * (len(L)+1)
dp1[0] = 1
for i in range(1, len(L)+1):
    dp0[i] = dp0[i-1] * 3 if L[i-1] == '0' else dp0[i-1] * 3 + dp1[i-1]
    dp0[i] %= mod
    dp1[i] = dp1[i-1] if L[i-1] == '0' else dp1[i-1] * 2
    dp1[i] %= mod
print((dp0[-1] + dp1[-1]) % mod)
