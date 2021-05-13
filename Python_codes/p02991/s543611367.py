"""
これは、3の倍数かつ最小ステップでTにたどりつけ、という問題。
拡張ダイクストラを使えばよい。
"""
from collections import deque
N,M = map(int,input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    edges[u].append(v)
visited = set()
S,T = map(int,input().split())
que = deque([(S,0)])
while que:
    cur,step = que.popleft()
    rest = step%3
    if cur == T and rest == 0:
        print(step//3)
        exit()
    if (cur,rest) in visited:
        continue
    else:
        visited.add((cur,rest))
        for nx in edges[cur]:
            que.append((nx,step+1))
print(-1)