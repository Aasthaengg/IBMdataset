import math
N = int(input())
P = [tuple(map(int, input().split())) for _ in range(N)]
DONE = (1 << N) - 1

ds = []
todo = [(0, i, (1 << i)) for i in range(N)]
while todo:
    d, i, state = todo.pop()
    x, y = P[i]
    for ni in range(N):
        if state & (1 << ni):
            continue
        nx, ny = P[ni]
        nd = d + math.sqrt((x - nx) ** 2 + (y - ny) ** 2)
        nstate = state | (1 << ni)
        if nstate == DONE:
            ds.append(nd)
        else:
            todo.append((nd, ni, nstate))
ans = math.fsum(ds) / len(ds)
print(ans)