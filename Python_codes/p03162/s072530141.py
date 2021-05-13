n = int(input())
a = [None]*n
b = [None]*n
c = [None]*n
for i in range(n):
    a[i],b[i],c[i] = list(map(int,input().split(' ')))

dp = [[0]*n for i in range(3)]
dp[0][0], dp[1][0], dp[2][0] = a[0],b[0],c[0]
for i in range(1,n):

    for j in range(3):
        if j==0:
            dp[j][i] = max(dp[1][i-1]+a[i], dp[2][i-1]+a[i])
        elif j==1:
            dp[j][i] = max(dp[0][i-1]+b[i], dp[2][i-1]+b[i])
        elif j==2:
            dp[j][i] = max(dp[0][i-1]+c[i], dp[1][i-1]+c[i])
print(max(dp[0][-1], dp[1][-1], dp[2][-1]))