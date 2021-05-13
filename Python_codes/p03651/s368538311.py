from math import gcd
n,k=map(int,input().split())
*a, =map(int,input().split())
a=sorted(a)
for i in range(len(a)):
  if i==0: tmp=a[0]
  else:
    tmp=gcd(tmp,a[i])
if k%tmp!=0 or max(a)<k:
  print("IMPOSSIBLE")
else: print("POSSIBLE")
