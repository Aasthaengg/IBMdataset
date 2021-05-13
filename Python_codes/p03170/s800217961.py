import resource
import sys
from functools import lru_cache
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.reverse()
sys.setrecursionlimit(1000000)

@lru_cache(maxsize=None)
def f(k, p):
  for a in A:
    if k >= a:
      if f(k-a, p ^ 1) == p:
        return p
  return p ^ 1

print('First' if f(K, 0) == 0 else 'Second')
