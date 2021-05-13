N,K=map(int,input().split())
A=list(map(int,input().split()))

if (A.index(1)+1)>=K and (N-A.index(1))>=K:
  ans=-(-A.index(1))//(K-1)-(-N+A.index(1)+1)//(K-1)
else:
  ans=1-(-N+K)//(K+1)
print(ans)