import sys
input = sys.stdin.readline

H, W, D = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
loc = [None] * (H*W+1)
for y in range(H):
    for x in range(W):
        loc[A[y][x]] = (x, y)
power = [0] * (H*W+1)
for n in range(D+1, H*W+1):
    i, j = loc[n-D]
    x, y = loc[n]
    power[n] = power[n-D] + abs(x-i) + abs(y-j)
Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    print(power[R] - power[L])
