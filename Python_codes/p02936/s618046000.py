import sys

input = sys.stdin.readline
n, q = map(int, input().split())

edges = [[] for _ in range(n)]
for _ in range(n - 1):
    frm, to = map(int, input().split())
    # 0-index
    edges[frm - 1].append(to - 1)
    edges[to - 1].append(frm - 1)


scores = [0] * n
for _ in range(q):
    v, s = map(int, input().split())
    scores[v - 1] += s


stack = [0]
visited = [False] * n
visited[0] = True
while len(stack):
    frm = stack.pop()
    for to in edges[frm]:
        if not visited[to]:
            scores[to] += scores[frm]
            visited[to] = True
            stack.append(to)


print(" ".join([str(w) for w in scores]))