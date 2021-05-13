n = int(input())
l = list(map(int,input().split()))
dp = [0] * n
 
dp[1] = abs(l[0] - l[1])
 
for i in range(2,n):
    a = abs(l[i] - l[i-2]) + dp[i-2]
    b = abs(l[i] - l[i-1]) + dp[i-1]
    if a <= b:
        dp[i] = a
    else:
        dp[i] = b
 
print(dp[-1])