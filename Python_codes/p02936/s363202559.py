from collections import deque, defaultdict
N, Q = map(int, input().split())
G = defaultdict(lambda: deque())
for _ in range(N-1):
    a,b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
   
cnt = [0]*(N+1)
for _ in range(Q):
    p, x = map(int, input().split())
    cnt[p] += x

def dfs(v, cnt):
    seen = [0] * (N+1)
    seen[v] = 1
    stack = [v]
    while stack:
        v = stack[-1]
        if G[v]:
            w = G[v].popleft()
            if not seen[w]: # if 訪れていなければ
                cnt[w] += cnt[v]
                seen[w] = 1
                stack.append(w)
        else:
            stack.pop()
    return cnt

cnt = dfs(1, cnt)
print(*cnt[1:])