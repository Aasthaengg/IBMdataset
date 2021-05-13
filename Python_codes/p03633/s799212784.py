def gcd(a,b):
  x=max(a,b)
  y=min(a,b)
  while y>0:
    x=x%y
    x,y=y,x
  return x

n=int(input())
t=[int(input()) for _ in range(n)]
lcm=t[0]
for i in range(1,n):
  lcm=(lcm*t[i])//gcd(lcm,t[i])
print(lcm)