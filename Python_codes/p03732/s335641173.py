import functools
from collections import*
@functools.lru_cache(maxsize=None)
def Knapsack(N,W):
    for i in range(N):
        w,v=map(int,input().split())
        for k,b in d.copy().items():
            if k+w<=W:
                d[k+w]=max(d[k+w],b+v)
    return max(d.values())
N,W=map(int,input().split())   #pypyで実行！
d=defaultdict(int)
d[0]=0
print(Knapsack(N,W))