import fractions as f
n,m=map(int,input().split())
a=list(map(int,input().split()))
g=1
def check(n):
  cnt=0
  while n%2==0:
    n//=2
    cnt+=1
  return cnt
chk=check(a[0])
for i in a:
  if chk!=check(i):
    print(0)
    exit()
  else:
    chk=check(i)
for i in range(n):
  g=g*(a[i]//2)//(f.gcd(g,a[i]//2))
  if g>m:print(0);exit()
print(m//g-m//(2*g))
