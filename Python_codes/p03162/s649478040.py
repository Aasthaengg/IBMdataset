n=int(input())
happy=[list(map(int,input().split())) for _ in range(n)]
DP=[[0,0,0] for _ in range(n+1)]
for i in range(n):
    a,b,c=happy[i]
    DP[i+1][0]=max(DP[i][1],DP[i][2])+a
    DP[i+1][1]=max(DP[i][2],DP[i][0])+b
    DP[i+1][2]=max(DP[i][0],DP[i][1])+c
print(max(DP[-1]))