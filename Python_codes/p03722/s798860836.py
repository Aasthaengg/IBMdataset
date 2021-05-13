import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect_left
from heapq import heappush, heappop

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def BellmanFord(E, N, source):
    #E:E[a]は頂点aを始点とする辺のリストであり、辺の終点bと辺の重みwが(b, w)の形で格納されている
    #N:頂点の数
    #source:始点
    #グラフの初期化
    d = [INF for _ in range(N)]
    d[source] = 0
    
    #辺の緩和
    for i in range(N):
        for j in range(N):
            e = E[j]
            if len(e) == 0:
                continue
            for edge in e:
                if d[edge[0]] > d[j] + edge[1]:
                    d[edge[0]] = d[j] + edge[1]
                    if i == N-1 and edge[0] == N-1:
                        return -1
    
    return d

N, M = MAP()
abc = [LIST() for _ in range(M)]
G = [[] for _ in range(N)]

for a, b, c in abc:
	G[a-1].append((b-1, -c))

dist = BellmanFord(G, N, 0)
if dist == -1:
	print("inf")
else:
	print(-dist[N-1])
