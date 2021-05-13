# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
XYH = [lr() for _ in range(N)]
height = [x for x in XYH if x[2] > 0]
zero = [x for x in XYH if x[2] == 0]
answer = None
for x in range(101):
    for y in range(101):
        bl = True
        top = height[0]
        cand = abs(x-top[0]) + abs(y-top[1]) + top[2]
        for x2, y2, h in height[1:]:
            temp = abs(x-x2) + abs(y-y2) + h
            if cand != temp:
                bl = False
                break
        if not bl:
            continue
        for x2, y2, h in zero:
            temp = abs(x-x2) + abs(y-y2) + h
            if temp < cand:
                bl = False
                break
        if bl:
            answer = (x, y, cand)

print(*answer)

