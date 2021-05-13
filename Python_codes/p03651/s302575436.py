import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
t=a[0]
for i in range(1,n):
  t=math.gcd(t,a[i])
if k%t!=0 or k>max(a):
  print('IMPOSSIBLE')
else:
  print('POSSIBLE')