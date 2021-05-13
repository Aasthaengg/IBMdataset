_,*l=map(int,open(0).read().split())
def f(s):
  c=t=0
  for i in l:
    t+=i
    if s*t<=0: c+=abs(t-s); t=s
    s*=-1
  return c
print(min(f(1),f(-1)))