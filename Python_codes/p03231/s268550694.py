from fractions import gcd
n,m = map(int,input().split())
s = input()
t = input()

g = gcd(n,m)
l = n*m//g

n2,m2 = l//n,l//m
g2 = gcd(n2,m2)
l2 = n2*m2//g2

ans = l
for i in range(l//l2):
  if s[i*l2//n2] != t[i*l2//m2]:
    ans = -1
    break
print(ans)

