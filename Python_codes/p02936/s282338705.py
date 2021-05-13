from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())

graph   = [ [] for _ in range(N) ]
queries = { p: 0 for p in range(N) }

for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())

    graph[a].append(b)
    graph[b].append(a)

for _ in range(Q):
    p, x = map(int, input().split())

    queries[p - 1] += x

answer = [ 0 ] * N

def dfs(p, p_before, acc):
    acc += queries[p]

    answer[p] = acc

    for child in graph[p]:
        if child == p_before:
            continue

        dfs(child, p, acc)

dfs(0, -1, 0)

print(*answer)