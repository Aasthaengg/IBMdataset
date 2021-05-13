n = int(input())
l = [int(x) for x in input().split()] 
dp = [float('inf')] * n  
dp[0] = 0
for i in range(n):
    for j in (i+1, i+2):
        if j < n:
            dp[j] = min(dp[j], dp[i]+abs(l[i]-l[j]))
print(dp[n-1])