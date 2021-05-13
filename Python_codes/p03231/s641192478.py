import math
n,m = map(int, input().split())
s = input()
t = input()

ans = int((n*m)/math.gcd(n,m))
g = math.gcd(n,m)
for i in range(g):
  if s[i*(n//g)] != t[i*(m//g)]:
    print (-1)
    exit()
print (ans)