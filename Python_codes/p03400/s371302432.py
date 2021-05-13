N=int(input())
D,X=map(int,input().split())
A=[int(input()) for _ in range(N)]
ans=0
for i in range(N):
  for j in range(D):
    if D>A[i]*j:
      ans+=1
    else:
      break
print(ans+X)