N,X=map(int,input().split())
A=list(map(int,input().split()))
ans=max(A[0]-X,0)
A[0]=min(X,A[0])
for i in range(1,N):
  a=A[i-1]
  b=A[i]
  if a+b>X:
    ans+=b-(X-a)
    A[i]=X-a
print(ans)