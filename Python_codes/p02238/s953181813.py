from collections import Counter
import sys

def input():
    return sys.stdin.readline().strip()

def dfs(v):
    start[v] = lb()
    for w in g[v]:
        if start[w] != None:
            continue
        dfs(w)
    end[v] = lb()

n = int(input())
g = [None] * (n+1)
start = [None] * (n+1)
end = [None] * (n+1)
lb = iter(range(1,2*n+1)).__next__
for _ in range(n):
    u,k,*vk = map(int,input().split())
    g[u] = vk
for v in range(1,n+1):
    if start[v] != None:
        continue
    dfs(v)

for i in range(1,n+1):
    print(i,start[i],end[i])
