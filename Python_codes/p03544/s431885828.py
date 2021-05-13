from functools import lru_cache

N = int(input())

@lru_cache(maxsize=None)
def luca(N):
  if N>=2:
    return luca(N-2)+luca(N-1)
  if N==1:
    return 1
  if N==0:
    return 2
  
print(luca(N))
