# https://atcoder.jp/contests/abc112/tasks/abc112_c
import sys
n = int(input())
pyramid = []
ch = 1
for _ in range(n):
    x, y, h = map(int, input().split())
    pyramid.append((x, y, h))
    ch = max(ch, h)

def cal(cx, cy, ch, x, y, h):
    height = max(ch - abs(x - cx) - abs(y - cy), 0)
    return height == h

while True:
    for cx in range(100 + 1):
        for cy in range(100 + 1):
            for x, y, h in pyramid:
                if not cal(cx, cy, ch, x, y, h):
                    break
            else:
                print(cx, cy, ch)
                sys.exit()
    ch += 1