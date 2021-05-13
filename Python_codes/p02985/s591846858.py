import sys
input = sys.stdin.readline
from collections import *

def P(n, r):
    res = 1
    
    for i in range(r):
        res *= n-i
        res %= MOD
    
    return res

def bfs():
    q = deque([0])
    visited = [False]*N
    visited[0] = True
    ans = K
    
    while q:
        v = q.popleft()
        cnt = 0
        
        for nv in G[v]:
            if not visited[nv]:
                cnt += 1
                visited[nv] = True
                q.append(nv)
        
        if v==0:
            ans *= P(K-1, cnt)
            ans %= MOD
        else:
            ans *= P(K-2, cnt)
            ans %= MOD
            
    return ans

N, K = map(int, input().split())
MOD = 10**9+7
G = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

print(bfs())