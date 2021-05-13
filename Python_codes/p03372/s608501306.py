import sys
input = sys.stdin.readline

n, c = [int(x) for x in input().split()]
xv = [[0, 0]]
for _ in range(n):
    xv.append([int(x) for x in input().split()])
xv.sort()

from copy import deepcopy

xv_2 = [[0, 0]] + deepcopy(xv)[::-1]
for i in range(1, n + 1):
    xv_2[i][0] = c - xv_2[i][0]

xv_cumsum = [0]
xv_2_cumsum = [0]

for i in range(1, n + 1):
    xv_cumsum.append(xv_cumsum[-1] + xv[i][1])
    xv_2_cumsum.append(xv_2_cumsum[-1] + xv_2[i][1])

clock = [0]
anti_clock = [0]

for i in range(1, n + 1):
    clock.append(clock[-1] + xv[i][1] - (xv[i][0] - xv[i - 1][0]))

for i in range(1, n + 1):
    anti_clock.append(anti_clock[-1] + xv_2[i][1] - (xv_2[i][0] - xv_2[i - 1][0]))

for i in range(1, n + 1):
    clock[i] = max(clock[i], clock[i - 1])
    anti_clock[i] = max(anti_clock[i], anti_clock[i - 1])

ans = 0

for i in range(n):
    ans = max(ans, xv_2_cumsum[i] - 2*xv_2[i][0] + clock[n - i], xv_cumsum[i] -2*xv[i][0] + anti_clock[n - i])

print(ans)
