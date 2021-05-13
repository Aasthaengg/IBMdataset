N=int(input())
P= list(map(float,input().split()))
ans=[[0 for e in range(2*N+3)] for f in range(N+1)]
ans[0][N+1]=1
for n in range(1,N+1):
 for i in range(N+1-n,N+2+n):
  ans[n][i]=ans[n-1][i-1]*P[n-1]+ans[n-1][i+1]*(1-P[n-1])
t=0
for i in range(N+1,2*N+3):
 t+=ans[N][i]
print(t)
