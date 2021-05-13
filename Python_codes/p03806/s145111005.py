import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N,x,y = MI()
dp = [[[10**4]*401 for i in range(401)] for n in range(N+1)]
# dp[n][i][j] = 薬品1~nを用いて、タイプAをiグラム、タイプBをjグラムを作った時に必要な最小予算

dp[0][0][0] = 0
for n in range(1,N+1):
    a,b,c = MI()
    for i in range(401):
        for j in range(401):
            if i >= a and j >= b:
                dp[n][i][j] = min(dp[n-1][i][j],dp[n-1][i-a][j-b]+c)
            else:
                dp[n][i][j] = dp[n-1][i][j]

z = min(dp[N][x*i][y*i] for i in range(1,min(400//x,400//y)+1))
print(-1 if z == 10**4 else z)
