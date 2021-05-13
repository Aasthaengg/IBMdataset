from math import sqrt
N=int(input())
K=int(sqrt(N)+2)
ans=N
for i in range(1,K):
  if N%i==0:
    j=N//i
    ans=min(ans,(i-1) + (j-1))
print(ans)