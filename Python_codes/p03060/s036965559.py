N=int(input())
V=list(map(int, input().split()))
C=list(map(int, input().split()))
ans=0
for i in range(2**N):
  X=0
  for j in range(N):
    if (i>>j)&1:
      X+=(V[j]-C[j])
  ans=max(ans,X)
print(ans)