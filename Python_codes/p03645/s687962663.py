import sys

input = sys.stdin.readline
n, m = map(int, input().split())
x = set()
y = set()
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        x.add(b)
    if b == n:
        y.add(a)
print(("POSSIBLE", "IMPOSSIBLE")[len(x & y) == 0])
