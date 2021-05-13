#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n,m = readInts()
G = [[] for _ in range(n)]
for i in range(m):
    a,b = map(lambda x:int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)
q = deque([0])
def pa():
    while q:
        v = q.popleft()
        for nv in G[v]:
            if arrived[nv] < 0:
                arrived[nv] = v + 1
                q.append(nv)
arrived = [-1] * n
pa()
if -1 in arrived[1:]:
    print('No')
else:
    print('Yes')
    print(*arrived[1:],sep='\n')
