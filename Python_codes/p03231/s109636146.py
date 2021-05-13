import math,sys
a,b=map(int,input().split())
s=input()
k=input()
t=math.gcd(a,b)
for i in range(t):
  if s[i*a//t]!=k[i*b//t]:
    print(-1)
    sys.exit()
print(a*b//t)