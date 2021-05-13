from math import log10
n,m = map(int,input().split())
a = list(map(int,input().split()))
l = [0,2,5,5,4,5,6,3,7,6]

dp = [0]*(n+1)
for i in range(n):
    for j in range(m):
        if dp[i] == 0 and i != 0:
            continue
        x = a[j]
        t = l[x]
        if i+t > n:
            continue
        if dp[i] == 0:
            s0 = x
            s1 = x
        else:
            k = int(log10(dp[i]))
            s0 = x*10**(k)+dp[i]
            s1 = 10*dp[i]+x
        dp[i+t] = max(dp[i+t],s0,s1)
print(dp[-1])