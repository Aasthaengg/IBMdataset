n = int(input())
C = []
mod = 10**9+7
for i in range(n):
    c = int(input())
    if i==0:
        C.append(c)
    elif C[-1]!=c:
        C.append(c)
n = len(C)
dp = [0]*n
idx = {}
for i in range(n):
    if i==0:
        idx[C[i]] = i
        dp[i] = 1
    else:
        if C[i] not in idx:
            dp[i] = dp[i-1]
            idx[C[i]] = i
        else:
            dp[i] = dp[i-1]+dp[idx[C[i]]]
            idx[C[i]] = i
print(dp[-1]%mod)