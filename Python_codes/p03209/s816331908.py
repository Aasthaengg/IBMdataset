n,x=map(int,input().split())
l=[1]
for i in range(50): l+=[l[-1]*2+3]
from functools import lru_cache
@lru_cache(None)
def f(n,x):
  return int(x>0) if n<1 else f(n-1,l[n-1])+1+f(n-1,x-l[n-1]-2) if x>l[n]//2 else f(n-1,x-1)
print(f(n,x))