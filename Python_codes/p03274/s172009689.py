N,K=map(int,input().split())
x = list(map(int,input().split()))
ans=10**10
for i in range(N+1-K):
 if x[i]>=0 and x[i-1+K]>=0 :
  ans=min(ans,max(x[i],x[i-1+K]))
 elif x[i]<=0 and x[i-1+K]<=0 :
  ans=min(ans,max(-x[i],-x[i-1+K]))
 else:
  ans=min(ans,x[i-1+K]-x[i]+min(x[i-1+K],-x[i]))
print(ans)
