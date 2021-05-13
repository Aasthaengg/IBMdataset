#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline()[:-1]
sys.setrecursionlimit(10**8)

n = int(input())
G1 = [0]*n
G2 = [[0]*n for i in range(n)]
d = [0]*n
f = [0]*n
for i in range(n):
    inp = tuple(map(int, input().split()))
    G1[inp[0]-1]=sorted(inp[2:])
time=0

def dfs(vertex):
    if d[vertex]:return
    global time
    time+=1
    d[vertex]=time
    for v in G1[vertex]:
        if not d[v-1]:
            dfs(v-1)
    time+=1
    f[vertex]=time
    return

for i in range(n):
    dfs(i)
for i in range(n):
    print(i+1,d[i],f[i])
    
    

