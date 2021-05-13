import sys
sys.setrecursionlimit(1000000000)
N=int(input())
ABC=[]
for _ in range(N):
    ABC.append(list(map(int,input().split())))
from functools import lru_cache
@lru_cache(maxsize=None)
def dynam(n):
    if n>1:
        a=max(dynam(n-1)[1]+ABC[n-1][0],
              dynam(n-1)[2]+ABC[n-1][0])
        b=max(dynam(n-1)[0]+ABC[n-1][1],
              dynam(n-1)[2]+ABC[n-1][1])
        c=max(dynam(n-1)[0]+ABC[n-1][2],
              dynam(n-1)[1]+ABC[n-1][2])
        return (a,b,c)
    return tuple(ABC[0])
print(max(dynam(N)))