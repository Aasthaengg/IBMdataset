#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 08:50:44 2020

@author: naoki
"""
from collections import deque

N = int(input())
uvws = [list(map(int, input().split())) for _ in range(N-1)]

routes = [[] for _ in range(N)]
for uvw in uvws:
    u = uvw[0]-1
    v = uvw[1]-1
    w = uvw[2]
    
    routes[u].append([v,w])
    routes[v].append([u,w])
    
    
colors = [-1 for _ in range(N)]
todo = deque()
todo.append(0)
colors[0] = 0


while len(todo)>0:
    checking = todo.pop()
    for route in routes[checking]:
        destination = route[0]
        weight = route[1]
        
        if colors[destination] == -1:
            if weight%2 == 0:
                colors[destination] = colors[checking]
            else:
                colors[destination] = 1 - colors[checking]
            todo.append(destination)

for i in range(N):
    print(colors[i])