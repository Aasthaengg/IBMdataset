N=int(input())
CARD={}
for i in range(N):
  s = str(input())
  if s not in CARD:
    CARD[s] = 1
  else:
    CARD[s]+=1
M=int(input())
for i in range(M):
  t = str(input())
  if t in CARD:
    CARD[t]-=1
print(max(max(CARD.values()),0))