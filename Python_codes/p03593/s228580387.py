import sys
from collections import Counter

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))  # applies to only numbers
rs = lambda: stdin.readline().rstrip()  # ignores trailing space

H, W = rl()
l = []
for _ in range(H):
    l.extend(list(rs()))

c = Counter(l)
count = W//2 * H
pair = 0
four = 0
for x in c.values():
    four += x // 4
    pair += x // 2

f = H // 2 * (W // 2)
if f > four:
    print('No')
    exit()

pair -= f * 2 #残りのペア
p = W // 2 if H&1 else 0
p += H // 2 if W&1 else 0
if p > pair:
    print('No')
    exit()

print('Yes')
# 16