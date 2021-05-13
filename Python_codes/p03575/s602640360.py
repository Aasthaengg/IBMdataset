def Graph(ab):
    G = [[] for i in range(n)]
    for a, b in ab:
        G[a - 1].append(b)
        G[b - 1].append(a)
    return G

from collections import deque
def dfs(pair):
    q = deque()
    q.append((1, -1, 0))
    log = [0] * n
    log[0] = 1
    while q:
        V, P, S = q.popleft()
        if S == 0:
        #下に遷移していく処理
        #q.append((V, P, 1))
            for new_v in G[V - 1]:
                if new_v == P:continue
                if set(pair) == {V, new_v}:continue 
                if log[new_v - 1]:continue 
                log[new_v - 1] = 1
                q.append((new_v, V, 0))
    return sum(log) == n 


n, m = map(int,input().split())
ab = [tuple(map(int,input().split())) for _ in range(m)]
G = Graph(ab)

res = 0
for t in ab:
    if dfs(t):
        #print(t)
        continue
    res += 1
print(res)