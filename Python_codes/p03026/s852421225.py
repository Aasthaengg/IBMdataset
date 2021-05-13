from collections import deque
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

d = list(map(int, input().split()))
d.sort(reverse=True)

que = deque()
que.append(0)
seen = [False for _ in range(n)]
seen[0] = True
memo = [0]
while que:
    cur = que.popleft()
    for to in edges[cur]:
        if seen[to]:
            continue
        seen[to] = True
        memo.append(to)
        que.append(to)


print(sum(d) - d[0])

ans = [0 for _ in range(n)]
for i in range(n):
    ans[memo[i]] = d[i]

print(*ans)