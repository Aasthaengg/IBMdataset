from fractions import gcd
N = int(input())
t, a = map(int, input().split())
x = gcd(t,a)
pT = t//x
pA = a//x
for i in range(1,N):
  t, a = map(int, input().split())
  mt = pT//t+1 if pT%t!=0 else pT//t
  ma = pA//a+1 if pA%a!=0 else pA//a
  m = max(mt,ma)
  pT = t*m
  pA = a*m

print(pT+pA)