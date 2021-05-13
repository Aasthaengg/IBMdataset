N,K=map(int,input().split())
x=list(map(int,input().split()))
ans=0
j=0
for i in range(N):
  if i==K-1:
    ans=min(abs(x[K-1]-x[0])+abs(x[K-1]),abs(x[K-1]-x[0])+abs(x[0]))
  elif i>=K:
    bns=min(abs(x[i]-x[i-K+1])+abs(x[i]),abs(x[i]-x[i-K+1])+abs(x[i-K+1]))
    ans=min(ans,bns)
print(ans)