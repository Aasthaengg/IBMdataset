#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:47:41 2020

@author: naoki
"""
import sys
import copy
def func():
    N, M = map(int, input().split())
    uvs = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    S, T = map(lambda x:int(x)-1, input().split())
    
    roots = [[] for _ in range(N)]
    
    for uv in uvs:
        roots[uv[0]].append(uv[1])
    
    costs = [-10000]*(N)
    
    from collections import deque
    
    todo = deque([S])
    costs[S] = 0
    todo_set = set([S])
    
    layers = [set() for _ in range(3)]
    
    while len(todo)>0:
        checking = todo.popleft()
        next_targets = deque([checking])
        for i in range(3):
            purposes = set()
            while len(next_targets) > 0:
                now = next_targets.pop()
                for root in roots[now]:
                    if root not in layers[i]:
                        layers[i].add(root)
                        purposes.add(root)
            next_targets = purposes.copy()
        for next_target in next_targets:
            if costs[next_target] < 0 and next_target not in todo_set:
                costs[next_target] = costs[checking]+1
                todo.append(next_target)
                todo_set.add(next_target)
                if next_target == T:
                    print(costs[next_target])
                    sys.exit()
    print(-1)
if __name__ == "__main__":
    func()