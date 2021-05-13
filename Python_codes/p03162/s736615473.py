n=int(input())
l=[]
for _ in range(n):
    temp=list(map(int,input().split()))
    l.append(temp)
dp=[[0]*3 for _ in range(n)]

dp[0][0],dp[0][1],dp[0][2]=l[0]

for i in range(n-1):
    for j in range(3):
        for k in range(3):
            if j==k: continue
            dp[i+1][k]=max(dp[i+1][k],dp[i][j]+l[i+1][k])
print(max(dp[n-1]))
