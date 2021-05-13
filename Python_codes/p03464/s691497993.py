#!/usr/bin/env python3
import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n = int(input())
A = list(map(int,input().split()))
A.reverse()

M = m = 2
for i,ai in enumerate(A):
  # print(m , (m-1+ai)//ai*ai , M//ai*ai + ai-1 , M)
  if not (m <= (m-1+ai)//ai*ai<= M):
    print(-1);exit()
  M = M//ai*ai + ai-1
  m = (m-1+ai)//ai*ai
  # print(m,M,i)
print(m,M)

# # 最大ケースを求める
# M = 2
# for i,ai in enumerate(A):
#   if M < ai:
#     print(-1);exit()
#   M = M//ai*ai + ai-1
#   print(M,i)
# print(M)

# # 最小ケースを求める
# m = 2
# for i,ai in enumerate(A):
#   m = (m-1+ai)//ai*ai

# print(m,M)

