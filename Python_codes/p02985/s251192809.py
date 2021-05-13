N, K = map(int, input().split())
graph = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

stack = [0]
ans = K
mod = 10**9+7
r = [True] * N
r[0] = False
while stack:
    v = stack.pop()
    tmp = K - 1
    if v > 0:
        tmp -= 1
    for child in graph[v]:
        if r[child]:
            r[child] = False
            stack.append(child)
            ans *= tmp
            tmp -= 1
            ans %= mod
print(ans)
