N = int(input())
adj = [[] for _ in range(N)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((v, w))
    adj[v].append((u, w))

stack = [0]
color = [-1]*N
color[0] = 0
while stack:
    v = stack.pop()
    for child, w in adj[v]:
        if color[child] < 0:
            color[child] = (color[v] + w) % 2
            stack.append(child)

for i in color:
    print(i)