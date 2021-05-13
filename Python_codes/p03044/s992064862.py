N = int(input())
data = [[] for _ in range(N)]
for _ in range(N-1):
    p, q, w = map(int, input().split())
    p -= 1
    q -= 1
    data[p].append((q,w))
    data[q].append((p,w))

colors = [0]*N
visited = [0]*N
start = 0
next_set = [start]
while next_set:
    p = next_set.pop()
    visited[p] = 1
    color = colors[p]
    for q, w in data[p]:
        if visited[q]:
            continue
        colors[q] = (color + w%2)%2
        next_set.append(q)
print(*colors, sep="\n")
