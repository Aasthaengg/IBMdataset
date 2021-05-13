import sys
input = sys.stdin.readline

N = int(input())
x, y, h = zip(*[list(map(int, input().split())) for _ in range(N)])
j = -1
for i in range(N):
    if h[i] != 0:
        j = i
        break
for cx in range(101):
    for cy in range(101):
        H = h[j] + abs(x[j] - cx) + abs(y[j] - cy)
        for i in range(N):
            if h[i] != max(H - abs(x[i] - cx) - abs(y[i] - cy), 0):
                break
        else:
            print(cx, cy, H)

