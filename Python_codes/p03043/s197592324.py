def kaisu(n,k):
  if n>=K:
    return k
  else:
    return kaisu(2*n,k+1)
N,K=map(int,input().split())
ans=0
for i in range(1,N+1):
  ans+=pow(2,20-kaisu(i,0))
ans=ans/(pow(2,20))
print(ans/N)