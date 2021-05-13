import math
n=int(input())
dp=[[0]*3 for i in range(n+1)]
s=[]
for i in range(n):
    arr=list(map(int,input().split()))
    s.append(arr)

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            dp[i+1][j]=max(dp[i][k]+s[i][j],dp[i+1][j])
print(max(dp[n]))