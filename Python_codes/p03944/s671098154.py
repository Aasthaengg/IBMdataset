#!/usr/bin/env python3
w, h, n = map(int, input().split())
xya = [map(int, input().split()) for _ in range(n)]
x, y, a = [list(i) for i in zip(*xya)]

arr = [[0] * w for i in range(h)]

for i in range(n):
    if a[i] == 1:
        for j in range(h):
            for k in range(x[i]):
                arr[j][k] = 1
    
    elif a[i] == 2:
        for j in range(h):
            for k in range(x[i], w):
                arr[j][k] = 1

    elif a[i] == 3:
        for j in range(y[i]):
            arr[j] = [1 for _ in arr[j]]

    elif a[i] == 4:
        for j in range(y[i], h):
            arr[j] = [1 for _ in arr[j]]

ans = 0
for s in arr:
    ans += s.count(0)

print(ans)