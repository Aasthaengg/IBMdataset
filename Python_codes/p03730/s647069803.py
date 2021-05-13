import math
a,b,c=map(int,input().split())
n=math.gcd(a,b)
if c%n!=0:
  print("NO")
else:
  print("YES")