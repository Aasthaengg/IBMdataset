import numpy as np
n = int(input())

sg = []

for i in range(n):
    x, l = map(int, input().split())
    sg.append([max(x - l, 0), x + l])

sg.sort(key=lambda x: x[1])

prev = sg[0][1]

ans = 0
for i in range(1, n):
    if prev > sg[i][0]:
        ans += 1
    else:
        prev = sg[i][1]

print(n - ans)