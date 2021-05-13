n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)


from collections import deque
seen = [False for _ in range(n)]
child = [[] for _ in range(n)]
par = [0 for _ in range(n)]
order = []
que = deque()
que.append(0)
seen[0] = True

while que:
    v = que.popleft()
    order.append(v)
    for to in edges[v]:
        if not seen[to]:
            seen[to] = True
            par[to] = v
            que.append(to)
            child[v].append(to)

d = [-1 for _ in range(n)]
c = [0 for _ in range(n)]
for i in order:
    d[i] = d[par[i]] + 1
for i in order[::-1]:
    if len(child[i]) == 0:
        continue
    for ch in child[i]:
        c[i] += c[ch] + 1



point = n - 1
move_s = (d[n-1] - 1) // 2
move_f = d[n-1] - 1 - move_s
for i in range((d[n-1] - 1) // 2):
    point = par[point]

cnt_s = c[point]
cnt_f = n - (c[point] + 1) - 1


print('Fennec' if cnt_f > cnt_s else 'Snuke')