#from heapq import heapify,heappush,heappop
N = int(input())

D = {}
for i in range(N):
  s = input()
  if s in D:
    D[s] += 1
  else:
    D[s] = 1
  
M = int(input())
for i in range(M):
  t = input()
  if t in D:
    D[t] -= 1
  else:
    D[t] = 1

print(max(max(D.values()),0))