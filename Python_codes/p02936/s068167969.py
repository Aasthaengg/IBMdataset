from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n, q = MAP()
graph = [[] for i in range(n)]
point = [0]*n
for i in range(n-1):
    a, b = MAP()
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
for i in range(q):
    p, x = MAP()
    point[p-1] += x

# dfsを用いて累積和を計算する
# 初期状態だと前の値がないためデフォルト引数に-1を代入
def dfs(now, prev = -1):
    for next in graph[now]:
        # 次のノードが前に参照した値の時はcontinue
        if next == prev:
            continue
        # 現在の値を次のポイントに加算することで累積和をとる
        point[next] += point[now]
        # 次のノードと現在のノードを引数にdfsを継続する
        dfs(next, now)

dfs(0)
print(*point)