import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())

XL = []
for _ in range(N):
    x, l = map(int, input().split())
    XL.append((x-l, x+l))

XL.sort(key=lambda x: x[1])

ans = 0
cur = -1e9
for i in range(N):
    if cur <= XL[i][0]:
        ans += 1
        cur = XL[i][1]
print(ans)
