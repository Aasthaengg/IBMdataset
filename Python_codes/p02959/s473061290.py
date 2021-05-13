N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans,res=0,0
if A[0]<=B[0]:
  ans+=A[0]
  res=B[0]-A[0]
else:
  ans+=B[0]
for i in range(1,N):
  if res>=A[i]:
    res=B[i]
    ans+=A[i]
  else:
    ans+=res
    A[i]-=res
    if A[i]<=B[i]:
      ans+=A[i]
      res=B[i]-A[i]
    else:
      ans+=B[i]
      res=0
if res>=A[N]:
  ans+=A[N]
else:
  ans+=res
print(ans)
