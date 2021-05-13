n = int(input())
H = [0]+list(map(int,input().split()))

if n >= 3:
    dp = [0]*(n+1)
    dp[2] = abs(H[2]-H[1])
    dp[3] = min(abs(H[3]-H[2])+dp[2], abs(H[3]-H[1]))
    for i in range(4,n+1):
        dp[i] = min(abs(H[i]-H[i-1])+dp[i-1], abs(H[i]-H[i-2])+dp[i-2])
    print(dp[n])
else:
    print(abs(H[2]-H[1]))