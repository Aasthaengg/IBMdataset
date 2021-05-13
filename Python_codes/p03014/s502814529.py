from itertools import chain

H,W = map(int,input().split())
grid = tuple(tuple(map(lambda c: c != '#', input())) for _ in range(H))

scores = [[0]*W for _ in range(H)]

for i in range(H):
    s = 0
    for j in range(W):
        if grid[i][j]:
            scores[i][j] += s
            s += 1
        else:
            s = 0

for i in range(H):
    s = 0
    for j in reversed(range(W)):
        if grid[i][j]:
            scores[i][j] += s
            s += 1
        else:
            s = 0

for j in range(W):
    s = 0
    for i in range(H):
        if grid[i][j]:
            scores[i][j] += s
            s += 1
        else:
            s = 0

for j in range(W):
    s = 0
    for i in reversed(range(H)):
        if grid[i][j]:
            scores[i][j] += s
            s += 1
        else:
            s = 0


print(1 + max(chain.from_iterable(scores)))
