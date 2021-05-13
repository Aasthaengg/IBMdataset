L = list(input())
k = len(L)
mod = 10**9+7
dp1 = [0]*(len(L)+1)
dp2 = [0]*(len(L)+1)
dp1[0] = 1

for i in range(len(L)):
    if L[i] == "1":
        dp1[i+1] = 2*dp1[i]
        dp2[i+1] = dp1[i] + 3*dp2[i]
    else:
        dp1[i+1] = dp1[i]
        dp2[i+1] = 3*dp2[i]
    dp1[i+1] %= mod
    dp2[i+1] %= mod

print((dp1[len(L)]+dp2[len(L)])%mod)