import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
MOD = 10**9+7
INF = float("inf")

N,M,P = map(int,(input().split()))
line = []
for i in range(M):
    a,b,c = map(int,(input().split()))
    line.append([a-1,b-1,-c+P])

min_distance = [INF]*N # min_distance[i] は始点から街iまでの最短距離
min_distance[0] = 0 # 始点から始点への最短距離は0とする

def Bellman_Ford():
    for _ in range(N):
        update = False
        for s,g,d in line: # [s,g,d] = [道路の始点,道路の終点,道路の長さ] について、すべての道路を見る
            if min_distance[s] != INF and min_distance[s] + d < min_distance[g]: # 最短経路が確立されている街から伸びる道路を通ることで、距離を短くできるならば、
                min_distance[g] = min_distance[s] + d # 最短距離を上書きする
                update = True
        if not update:
            flag = 1
            break

def Bellman_Ford2():
    for _ in range(N):
        for s,g,d in line: # [s,g,d] = [道路の始点,道路の終点,道路の長さ] について、すべての道路を見る
            if min_distance[s] != INF and min_distance[s] + d < min_distance[g]: # 最短経路が確立されている街から伸びる道路を通ることで、距離を短くできるならば、
                min_distance[g] = -INF
                if g == N-1:
                    break
        else:
            continue
        break

flag = 0
Bellman_Ford()

if flag == 1:
    ans = min_distance[N-1]
    print(max(-ans,0))
else:
    Bellman_Ford2()
    ans = min_distance[N-1]
    if ans == -INF:
        print(-1)
    else:
        print(max(-ans,0))

#print(min_distance)
