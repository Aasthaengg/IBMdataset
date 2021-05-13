import numpy as np

def func(x,y):
    if y-x == 2:
        return 1
    else:
        return 0


H,W = map(int,input().split())
l = [input() for i in range(H)]

d = np.zeros((H,W))
dp = np.zeros((H,W))

for i in range(H):
    for j in range(W):
        if l[i][j] == "#":
            d[i][j] = 1
        else:
            d[i][j] = -1



for i in range(H-1):
    dp[i+1][0] = dp[i][0]+func(d[i][0],d[i+1][0])

for i in range(W-1):
    dp[0][i+1] = dp[0][i]+func(d[0][i],d[0][i+1])

for i in range(H-1):
    for j in range(W-1):
        dp[i+1][j+1]=min(dp[i][j+1]+func(d[i][j+1],d[i+1][j+1]),dp[i+1][j]+func(d[i+1][j],d[i+1][j+1]))

a = int(dp[-1][-1])
if d[0][0] == 1:
    a +=1
print(a)
