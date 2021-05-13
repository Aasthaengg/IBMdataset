N=int(input())
A=list(map(int,input().split()))
l=abs(A[0])
ans=0
for i in range(N-1):
  if A[i]<0:
    ans-=A[i]
    A[i+1]*=-1
  else:
    ans+=A[i]
  l=min(abs(A[i]),l)
if A[-1]<0:
  ans+=-A[-1]-min(l,abs(A[-1]))*2
else:
  ans+=A[-1]
print(ans)