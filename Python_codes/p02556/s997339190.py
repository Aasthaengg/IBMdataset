import sys
from operator import itemgetter

N = int(input())
V = set()
for s in sys.stdin.readlines():
    x, y = map(int, s.split())
    V.add((x + y, x - y))

y1 = max(V, key=itemgetter(1))[1]
y2 = min(V, key=itemgetter(1))[1]
x1 = max(V, key=itemgetter(0))[0]
x2 = min(V, key=itemgetter(0))[0]

print(max(abs(x1 - x2), abs(y1 - y2)))
