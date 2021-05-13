from collections import Counter
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *l = map(int, read().split())

c = Counter(l)
sides = sorted([[x, y] for x, y in c.items() if y >= 2])
ans = 0

if len(sides) == 1:
    if sides[-1][1] >= 4:
        ans = sides[-1][0] ** 2
elif len(sides) >= 2:
    if sides[-1][1] >= 4:
        ans = sides[-1][0] ** 2
    else:
        ans = sides[-1][0]*sides[-2][0]
print(ans)