n=int(input())
l=[[int(i) for i in input().split()] for _ in range(n)]

dp=[0,0,0]
for i in range(n):
    nextdp=[]
    for j in range(3):
        x=dp[j+1:]+dp[:j]
        nextdp.append(max(x)+l[i][j])
    dp=nextdp

print(max(dp))    
