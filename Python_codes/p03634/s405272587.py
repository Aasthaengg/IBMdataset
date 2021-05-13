from sys import stdin
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
N = int(stdin.readline().rstrip())
adj = defaultdict(set)

for i in range(N-1):
    a,b,c = [int(x) for x in stdin.readline().rstrip().split()]
    adj[a].add((b,c))
    adj[b].add((a,c))
    
Q,K = [int(x) for x in stdin.readline().rstrip().split()]

visited = [False]*(N+1)
dist = [0]*(N+1)

def dfs(i,j):
    if visited[i]:
        return
    dist[i] = j
    visited[i] = True
    
    for node,d in adj[i]:
        dfs(node,d+j)
        
dfs(K,0)

for i in range(Q):
    x,y = [int(x) for x in stdin.readline().rstrip().split()]
    print(dist[x]+dist[y])