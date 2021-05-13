from collections import defaultdict,deque
from sys import stdin,setrecursionlimit
import heapq,bisect,math,itertools,string,queue,datetime,copy
setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, stdin.readline().split()))

N,M = inpl()
prefe = defaultdict(list)
for i in range(M):
    p,m = inpl()
    prefe[p].append((m,i+1))

anls = [[] for _ in range(M)]
for a,item in prefe.items():
    item.sort()
    jyun = []
    for b in item:
        ind = bisect.bisect_left(item,b) + 1
        jyun.append([ind,b[1]])
    for item2 in jyun:
        anls[item2[1]-1].append((a,item2[0]))

for item3 in anls:
    print(str(item3[0][0]).zfill(6) + str(item3[0][1]).zfill(6))
