from collections import defaultdict
N, K, L = map(int,input().split())
data = [[0, 0] for _ in range(N)]
Lpath = [[] for _ in range(N)]
Tpath = [[] for _ in range(N)]

for _ in range(K):
    p, q = map(int,input().split())
    p -= 1
    q -= 1
    Lpath[p].append(q)
    Lpath[q].append(p)
    
for _ in range(L):
    r, s = map(int,input().split())
    r -= 1
    s -= 1
    Tpath[r].append(s)
    Tpath[s].append(r)
    
for i in range(N):
    if data[i][0]:
        continue
    data[i][0] = i + 1
    stack = [i]
    while stack:
        s = stack.pop()
        for to in Lpath[s]:
            if data[to][0]:
                continue
            data[to][0] = i + 1
            stack.append(to)

for i in range(N):
    if data[i][1]:
        continue
    data[i][1] = i + 1
    stack = [i]
    while stack:
        s = stack.pop()
        for to in Tpath[s]:
            if data[to][1]:
                continue
            data[to][1] = i + 1
            stack.append(to)

ans = [0] * N
d = defaultdict(int)         
for i in range(N):
    d[tuple(data[i])] += 1
for i in range(N):
    ans[i] = d[tuple(data[i])]

print(*ans)