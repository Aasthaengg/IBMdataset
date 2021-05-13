import math
a,b,c,d=[int(x) for x in input().split()]

def div(n,p):
  return n//p

def lcm(x, y):
  return (x * y) // math.gcd(x, y)

ans=b-a+1
ans-=(div(b,c)-div(a-1,c))
ans-=(div(b,d)-div(a-1,d))
e=lcm(c,d)
ans+=(div(b,e)-div(a-1,e))
print(ans)