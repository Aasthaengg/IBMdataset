#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import defaultdict
import json
from copy import deepcopy
import sys
sys.setrecursionlimit(10**4)

def dfs(graph, s):
  dist = [-1 for _ in range(len(graph))]
  dist[s] = 0
  stack = [s]
  while len(stack) != 0:
    s = stack.pop()
    for t in graph[s]:
      dist[t] = dist[s]+1
      if s in graph[t]:
        graph[t].remove(s)
      stack.append(t)
  return dist

if __name__=='__main__':
  graph = defaultdict(list)
  n, u, v = map(int, input().strip().split())
  for _ in range(n-1):
    ai, bi = map(int, input().strip().split())
    graph[ai-1].append(bi-1)
    graph[bi-1].append(ai-1)
  du = dfs(deepcopy(graph), u-1)
  dv = dfs(deepcopy(graph), v-1)
  costv = [0]
  for duv, dvv in zip(du, dv):
    if duv < dvv:
      costv.append(dvv)
  print(max(costv) - 1)