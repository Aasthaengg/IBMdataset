import sys
from collections import defaultdict
int1 = lambda x: int(x) - 1
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(500000)

H, W = map(int, readline().split())
A = [readline().decode().rstrip() for _ in range(H)]

dicts = defaultdict(int)
for a in A:
    for c in a:
        dicts[c] += 1

g1 = H * W % 2
g2 = (H // 2) * (W % 2) + (W // 2) * (H % 2)
g4 = (H // 2) * (W // 2)

for _ in range(g1):
    for k, v in dicts.items():
        if (v % 4 == 1) | (v % 4 == 3):
            dicts[k] -= 1
            break

for _ in range(g2):
    for k, v in dicts.items():
        if v % 4 == 2:
            dicts[k] -= 2
            break
"""for _ in range(g4):
    for k, v in dicts.items():
        if (v % 4 == 0) & (v != 0):
            dicts[k] -= 4
            break
"""
for k, v in dicts.items():
    if v % 4 != 0:
        print('No')
        sys.exit()

print("Yes")
