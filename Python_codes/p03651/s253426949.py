import sys
import fractions

n,k = map(int,input().split())
a = list(map(int,input().split()))

if k > max(a) :
  print('IMPOSSIBLE')
  sys.exit()
if k in a :
  print('POSSIBLE')
  sys.exit()
  
g = fractions.gcd(a[0],a[1])
for i in range(2,n) :
  g = fractions.gcd(g,a[i])
  
if k%g == 0 :
  print('POSSIBLE')
else :
  print('IMPOSSIBLE')