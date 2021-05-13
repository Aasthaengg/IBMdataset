# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(100000)
N = int(input())
adj = [[0]*N for _ in range(N)]
searched = {n: 0 for n in range(N)}
edge = {}

for n in range(N):
    inp = list(map(int, input().split()))
    edge[n] = inp[1]
    for i in inp[2:]:
        adj[inp[0]-1][i-1] = 1

time = 1
stack = []
unsearch = set(range(N))
uncomplete = set(range(N))
result = {n:{"found": 0, "finish": 0} for n in range(N)}

def DFS(i):
    global time
    global unsearch
    
    itr = sorted(unsearch)
    
    for j in itr:
        if adj[i][j] == 1 and j in unsearch:
            result[j]["found"] = time
            time += 1
            unsearch.remove(j)
            DFS(j)
    result[i]["finish"] = time
    time += 1
    
while len(unsearch):
    i = min(unsearch)
    unsearch.remove(i)
    result[i]["found"] = time
    time += 1
    DFS(i)

for n in range(N):
    print("{} {} {}".format(n+1, result[n]["found"], result[n]["finish"])) 