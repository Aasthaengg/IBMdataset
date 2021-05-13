import collections

n,q = map(int, input().split())
cnt = [0] * (n+1)
g = [[] for _ in range(n+1)]

for _ in range(n-1):    #隣接リストの生成
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for _ in range(q):
    v,val = map(int, input().split())
    cnt[v] += val

q = collections.deque()
q.append(1)
checked = [0]*(n+1)

while q:
    v = q.pop()
    checked[v] = 1
    for u in g[v]:
        if checked[u] == 1:
            continue
        cnt[u] += cnt[v]
        q.append(u)
print(*cnt[1:])
