N=int(input())
P=[0]+list(map(float,input().split()))

DP=[[0]*(N+1) for _ in range(N+1)]
DP[0][0]=1

for i in range(N):
    for j in range(i+1):
        DP[i+1][j+1]+=DP[i][j]*P[i+1]
        DP[i+1][j]+=DP[i][j]*(1-P[i+1])

#for row in range(N+1):
    #string=''
    #for column in range(N+1):
        #string+=str(DP[row][column])+' '
    #print(string)

ans=0
half=(N+1)//2
for k in range(half,N+1):
    ans+=DP[N][k]

print(ans)