from functools import *
@lru_cache(maxsize=None) # memoization
def f(x):
  if x==0:return 0
  s=10000000000000000
  for u in [1]+[6**i for i in range(1,11)]+[9**i for i in range(1,11)]:
    if x-u>=0:
      s=min(s,f(x-u)+1)#min coins, coins dp
  return s
for i in range(1,100001):f(i)
print(f(int(input()))) # answer