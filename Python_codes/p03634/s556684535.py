n = int(input())
abc = [list(map(int, input().split())) for _ in range(n - 1)]
q, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(q)]

adj = [[] for _ in range(n)]
for a, b, c in abc:
    a -= 1
    b -= 1
    adj[a].append([b, c])
    adj[b].append([a, c])


def dfs(s):
    d = [-1] * n
    d[s] = 0
    stack = [s]

    while stack:
        u = stack.pop()
        for v, c in adj[u]:
            if d[v] == -1:
                d[v] = d[u] + c
                stack.append(v)

    return d


d = dfs(k - 1)

for x, y in xy:
    x -= 1
    y -= 1
    print(d[x] + d[y])
