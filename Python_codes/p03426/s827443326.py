H, W, D = map(int, input().split())
A = []
N = (H * W)
indices = [None] * (N + 1)
for h in range(H):
    tmp = list(map(int, input().split()))
    A.append(tmp)
    for w in range(W):
        indices[tmp[w]] = (h, w)

d = [0] * (N + 1)
for i in range(D+1, N+1):
    y1, x1 = indices[i]
    y2, x2 = indices[i-D]
    d[i] = d[i-D] + abs(y1 - y2) + abs(x1 - x2)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(d[r] - d[l])