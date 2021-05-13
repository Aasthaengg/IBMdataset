N=int(input())
A=list(map(int,input().split()))
H=list(range(1,N+1))
c=0
ans=0
for i in range(N):
  if A[i]==H[c]:
    c+=1
  else:
    ans+=1
if ans==N:
  print("-1")
else:
  print(ans)