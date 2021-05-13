import math
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=a[0]
for m in a:
  c=math.gcd(c,m)
if k %c==0 and k<=max(a):
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")