from fractions import gcd
n,k,*a=map(int,open(0).read().split())
x=a[0]
if k>max(a):
  print('IMPOSSIBLE')
  exit()
for a_i in a:
  x=gcd(x,a_i)
if k%x==0:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')