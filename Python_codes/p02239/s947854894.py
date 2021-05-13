#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	breadth_first_search
# CreatedDate:  2020-04-14 23:40:14 +0900
# LastModified: 2020-04-15 00:14:09 +0900
#


import os
import sys
from collections import deque

def bfs(matrix,n):
    s=0
    color=[0]*n
    color[s]=1
    Q=deque()
    Q.append(s)
    distance = [-1]*n
    distance[0]=0
    while Q:
        u = Q.popleft()
        for v in matrix[u]:
            if color[v]==0:
#                print("{}->{}".format(u,v))
                distance[v]=distance[u]+1
                color[v]=1
                Q.append(v)
        color[u]=2
    
    return distance

def main():
    n=int(input())
    matrix = [[] for _ in range(n)]
    for i in range(n):
        lined = map(int,input().split())
#        print(lined)
        for j,pon in enumerate(lined):
            if j>=2:
                matrix[i].append(pon-1)
#    print(matrix)
    distance = bfs(matrix,n)
    for i,di in enumerate(distance):
        print("{} {}".format(i+1,di))

if __name__ == "__main__":
    main()

