N = 10**9+7

s = input()
l = len(s)
dp=[[0]*13 for i in range(l+1)]
dp[0][0]=1

c = 1
for i in range(l):
    x = s[-1-i]
    if x == '?':
        for k in range(10):
            for j in range(13):
                dp[i+1][(k*c+j)%13]+=dp[i][j]
                dp[i+1][(k*c+j)%13]%=N
    else:
        k = int(x)
        for j in range(13):
            dp[i+1][(k*c+j)%13]+=dp[i][j]
            dp[i+1][(k*c+j)%13]%=N
    c*=10
    c%=13
print(dp[l][5])
