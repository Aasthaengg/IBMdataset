N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N - 1)]
C = sorted([int(_) for _ in input().split()])
Pairs = [set() for _ in range(N)]
for a, b in AB:
    #0-indexed
    a -= 1
    b -= 1
    Pairs[a].add(b)
    Pairs[b].add(a)
visited = [False] * N
visited[0] = True
count = [0] * N
stack = [0]
start = []
parent = [0] * N
while stack:
    fr = stack.pop()
    updated = False
    for to in Pairs[fr]:
        if not visited[to]:
            visited[to] = updated = True
            stack += [to]
            count[fr] += 1
            parent[to] = fr
    if not updated:
        start += [fr]
order = []
while start:
    fr = start.pop()
    if count[fr]:
        continue
    order += [fr]
    to = parent[fr]
    count[to] -= 1
    start += [to]
ans = [0] * N
for i in range(N):
    ans[order[i]] = C[i]
score = 0
for a, b in AB:
    #0-indexed
    a -= 1
    b -= 1
    score += min([ans[a], ans[b]])
print(score)
print(*ans)
