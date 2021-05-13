from functools import lru_cache

n = int(input())
@lru_cache(maxsize=None)
def func(n):
  if n < 6:
    return n
  a = []
  b = 6
  while(b<=n):
    a.append(b)
    b*=6
  b = 9
  while(b<=n):
    a.append(b)
    b*=9
  ret = n
  a.sort(reverse=True)
  for i in a:
    ret = min(ret,1+func(n-i))
  return ret
print(func(n))