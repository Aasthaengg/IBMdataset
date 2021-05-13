import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

a, b, c, d, e, f = map(int, readline().split())
ans = [0, 0]
check = 0
S = set()
W = set()
for i in range(31):
    for j in range(31):
        if 100 * a * i + 100 * b * j <= f:
            W.add(100 * a * i + 100 * b * j)
for i in range(1501):
    for j in range(1501):
        if c * i + d * j <= f:
            S.add(c * i + d * j)
W = sorted(list(W))
S = sorted(list(S))
for w in W:
    for s in S:
        if w == 0:
            continue
        n = 100 * s / (w + s)
        if w + s > f or s > e * (w / 100):
            break
        if n > check:
            ans = w + s, s
            check = n
if ans[0] == 0:
    print(100 * a, ans[1])
else:
    print(*ans)
