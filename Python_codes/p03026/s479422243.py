from collections import deque
N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)
c = list(map(int, input().split()))
c.sort(reverse=True)
score = sum(c) - max(c)
num = [-1] * N
que = deque()
que.append(0)
i = 0
while que:
    v = que.pop()
    if num[v] != -1:
        continue
    num[v] = c[i]
    i += 1
    for nv in adj[v]:
        que.append(nv)
print(score)
print(*num)
