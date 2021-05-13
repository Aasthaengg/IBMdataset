import math
n,m = map(int,input().split())
s = input()
t = input()
lcm = int(n*m/math.gcd(n,m))
if (n-1)//(lcm//m) == 0:
  if s[0] == t[0]:
    print(lcm)
  else:
    print(-1)
else:
  for i in range((n-1)//(lcm//m)):
    if s[i*(lcm//m)] != t[i*(lcm//n)]:
      print(-1)
      exit()
    elif i == (n-1)//(lcm//m)-1:
      print(lcm)