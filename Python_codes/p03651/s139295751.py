N,K=map(int,input().split())
A=list(map(int,input().split()))
a=max(A)

import fractions
ans=A[0]
for i in range(1,N):
  ans=fractions.gcd(ans,A[i])
if K>a:
  print('IMPOSSIBLE')
  exit()
if (a-K)%ans==0:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')