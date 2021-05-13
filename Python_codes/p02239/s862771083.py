#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**8)
from collections import deque

n=int(input())
G=[0]*n
memo=[0]*n
dis=[0]*n
dis[0]=1
que=deque()
que.append((0,1))

for i in range(n):
    inp=tuple(map(int,input().split()))
    G[inp[0]-1]=inp[2:]

while que:
    vertex,d=que.popleft()
    for v in G[vertex]:
        if not dis[v-1]:
            dis[v-1]=d+1
            que.append((v-1,d+1))
        

for i in range(n):
    print(i+1,dis[i]-1)

