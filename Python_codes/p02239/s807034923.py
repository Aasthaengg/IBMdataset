from collections import deque

n = int(input())
g = [None] * (n+1)
ans = [0] * (n+1)

for _ in range(n):
    u,k,*vk = map(int,input().split())
    g[u] = vk

def bfs(now):
    que = deque()
    que.append(now)
    while que.__len__() != 0:
        now = que.popleft()
        for ne in g[now]:
            if ans[ne] != 0:
                continue
            ans[ne] = ans[now]+1
            que.append(ne)

bfs(1)
ans = [i if i != 0 else -1 for i in ans]
ans[1] = 0

print("\n".join("{} {}".format(*args) for args in zip(range(1, n+1), ans[1:])))
