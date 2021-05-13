N=int(input())
A=[int(input()) for i in range(N)]
if A[0]!=0:
  print(-1)
  exit()
ans=0
for i in range(N-1):
  if A[i+1]-A[i]>1:
    print(-1)
    exit()
  elif A[i+1]-A[i]==1:
    ans+=1
  else:
    ans+=A[i+1]
print(ans)