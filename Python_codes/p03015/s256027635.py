L = input()
n = len(L)
mod = 10**9+7
dp1 = [0]*(n+1)
dp2 = [0]*(n+1)
dp1[0] = 1
for i in range(n):
    if L[i] == "1":
        dp1[i+1] = (dp1[i]*2)%mod
        dp2[i+1] = (dp1[i] + dp2[i]*3)%mod
    else:
        dp1[i+1] = dp1[i]
        dp2[i+1] = (dp2[i]*3)%mod
print((dp1[n]+dp2[n])%mod)