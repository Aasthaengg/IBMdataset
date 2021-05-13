from functools import lru_cache
@lru_cache(maxsize=None)

def luca(n):
    if n==0:
        return 2
    elif n == 1:
        return 1
    else:
        return luca(n-1)+luca(n-2)

N = int(input())

print(luca(N))
