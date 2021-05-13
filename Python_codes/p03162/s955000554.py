N=int(input())
l=[[0,0,0]]+[list(map(int,input().split())) for _ in range(N)]

sum=[[0]*3 for _ in range(N+1)]
for i in range(1,N+1):
    sum[i][0]=max(sum[i-1][1],sum[i-1][2])+l[i][0]
    sum[i][1]=max(sum[i-1][0],sum[i-1][2])+l[i][1]
    sum[i][2]=max(sum[i-1][0],sum[i-1][1])+l[i][2]
ans=max(sum[N])
print(ans)