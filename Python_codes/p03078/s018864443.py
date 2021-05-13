#!/usr/bin/python3
# -*- coding:utf-8 -*-

import heapq

def main():
  na, nb, nc, K = map(int, input().split())
  As = sorted(list(map(int, input().split())), reverse=True)
  Bs = sorted(list(map(int, input().split())), reverse=True)
  Cs = sorted(list(map(int, input().split())), reverse=True)
  
  scores = [(-(As[0]+Bs[0]+Cs[0]), 0, 0, 0)]
  used = [(0, 0, 0)]
  def push(i, j, k):
    heapq.heappush(scores, (-(As[i] + Bs[j] + Cs[k]), i, j, k))
    
  for _ in range(K):
    (score, i, j, k) = heapq.heappop(scores)
    print(-score)
    for di, dj, dk in [[1,0,0], [0,1,0], [0,0,1]]:
      if not (i+di < na and j+dj<nb and k+dk < nc):
        continue        
      if (i+di, j+dj, k+dk) not in used:
        push(i+di, j+dj, k+dk)
        used.append((i+di, j+dj, k+dk))

if __name__=='__main__':
  main()

