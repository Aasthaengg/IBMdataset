n = int(input())
graph = [[] for _ in range(n)]
cnt = [0] * (n)
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

C = list(map(int, input().split()))
C.sort(reverse=True)
num = sum(C[1:])

ans = [0] * (n)

start = 0
par = [-1] * n
stack = [start]
idx = 0
ans[0] = C[idx]
idx += 1
while stack:
    v = stack.pop()
    for u in graph[v]:
        if u == par[v]:
            continue
        par[u] = v
        ans[u] = C[idx]
        idx += 1
        stack.append(u)
    # print(stack)

print(num)
print(*ans, sep=" ")
