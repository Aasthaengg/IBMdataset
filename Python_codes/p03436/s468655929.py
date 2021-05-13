import sys
from collections import deque


def input():
    return sys.stdin.readline()[:-1]


H, W = map(int, input().split())

white_cnt = 0
grid = [[] for i in range(H+2)]
check = [[0] * (W+2) for i in range(H+2)]
grid[0] = ['#']*(W+2)
for i in range(1, H+1):
    w = list(input())
    white_cnt += w.count('.')
    grid[i] = ['#'] + w + ['#']
grid[-1] = ['#']*(W+2)

mv_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
que_hwc = deque([(1, 1, 1)])
check[1][1] = 1
while que_hwc:
    hwc = que_hwc.popleft()
    h = hwc[0]
    w = hwc[1]
    cnt = hwc[2]
    if h == H and w == W:
        print(white_cnt-cnt)
        exit(0)

    for mv in mv_list:
        mv_h = h + mv[0]
        mv_w = w + mv[1]
        if grid[mv_h][mv_w] == '.' and check[mv_h][mv_w] != 1:
            check[mv_h][mv_w] = 1
            que_hwc.append((mv_h, mv_w, cnt+1))
print(-1)
