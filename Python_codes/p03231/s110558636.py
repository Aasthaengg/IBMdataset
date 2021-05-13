from  fractions  import gcd
n,m = map(int,input().split())
s = input()
t = input()
def lcm(x,y):
  return (x*y)//gcd(x,y)

a = lcm(n,m)
b = gcd(n,m)
if b==1:
  if s[0]==t[0]:
    print(a)
  else:
    print(-1)
else:
  k = int(a//b)
  for i in range(b):
    w = int(n*i//b)
    ww = int(m*i//b)
    if s[w]==t[ww]:
      continue
    else:
      print(-1)
      exit()
  else:
    print(a)