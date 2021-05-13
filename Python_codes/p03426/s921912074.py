# https://atcoder.jp/contests/abc089/tasks/abc089_d

H, W, D = map(int, input().split())
MAX = H * W + 1

d = [0] * (MAX + 1)
px = [None] * (MAX + 1)
py = [None] * (MAX + 1)

for h in range(H):
    Ah = list(map(int, input().split()))
    for w in range(W):
        px[Ah[w]] = h
        py[Ah[w]] = w

for i in range(D + 1, H * W + 1):
    d[i] = d[i - D] + abs(px[i] - px[i - D]) + abs(py[i] - py[i - D])

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(d[R] - d[L])