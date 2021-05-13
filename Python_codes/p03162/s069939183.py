N = int(input())
ls = [[0 for i in range(3)] for i in range(N)]
for i in range(N):
    ls[i] = list(map(int,input().split()))
# dp[i][j] -> i-1日目にjの仕事をしたときの i 日目の幸福度の総和
dp = [ [0 for i in range(3)] for i in range(N)]
for i in range(3):
    dp[0][i] = ls[0][i]
for i in range(1,N):
    for j in range(3):
        w = [0,1,2]
        w.remove(j)
        x,y = w[0],w[1]
        dp[i][j] = max(dp[i-1][x],dp[i-1][y]) + ls[i][j]
            
print(max(dp[N-1]))
