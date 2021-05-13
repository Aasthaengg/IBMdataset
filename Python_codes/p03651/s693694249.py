from fractions import gcd

N,K = map(int, input().split())
As = list(map(int,input().split()))

if K in As:
  print('POSSIBLE')
  exit()
if K > max(As):
  print('IMPOSSIBLE')
  exit()
  
r = As[0]

for i in range(1,N):
  r = gcd(As[i],r)
  
if K%r != 0:
  print('IMPOSSIBLE')
else:
  print('POSSIBLE')