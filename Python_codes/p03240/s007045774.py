import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
P = []
for _ in range(N):
    x, y, h = list(map(int, input().split()))
    P.append([x, y, h])
    if h != 0:
        tx, ty, th = x, y, h


for cx in range(101):
    for cy in range(101):
        H = th + abs(tx-cx)+abs(ty-cy)
        if all(h == max(H - abs(x - cx) - abs(y - cy), 0) for x, y, h in P):
            print(cx, cy, H)
            exit(0)
