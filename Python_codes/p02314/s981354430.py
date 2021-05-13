n = int(input().split()[0])
c = list(map(int,input().split()))
dp = [ i for i in range(n+1) ]

for i in range(2,n+1):
    c2 = filter(lambda n:n<=i,c)
    for j in c2:
        if j <= i and dp[i-j] + 1 < dp[i]:
            dp[i] = dp[i-j] + 1

print(dp[n])