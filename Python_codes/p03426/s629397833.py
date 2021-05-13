import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

H, W, D = map(int, readline().split())
A = [list(map(int, readline().split())) for _ in range(H)]
Q = int(readline())
query = [tuple(map(int, readline().split())) for _ in range(Q)]

path = [[(-1, -1)]*((H*W)//D+1) for _ in range(D)]
for i in range(H):
    for j in range(W):
        a = A[i][j]
        div, mod = divmod(a, D)
        path[mod][div] = (i, j)
path[0][0] = path[0][1]

cost = []
for i in range(D):
    tmp = [0]
    for l, r in zip(path[i][:-1], path[i][1:]):
        x, y = l
        z, w = r
        tmp.append(tmp[-1] + abs(z - x) + abs(w - y))
    cost.append(tmp)

ans = []
for L, R in query:
    vl, md = divmod(L, D)
    vr = R // D

    tmp = cost[md][vr] - cost[md][vl]
    ans.append(tmp)

print(*ans, sep="\n")
