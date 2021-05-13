import sys
sys.setrecursionlimit(500000)

N, Q = map(int, input().split())

tree = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

scores = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    scores[p-1] += x

ans = [0] * N
visited = set()
def dfs(n: int, score: int):
    score += scores[n]
    ans[n] = score
    visited.add(n)
    for v in tree[n]:
        if v not in visited:
            dfs(v, score)

dfs(0, 0)

print(*ans)