import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

l = list(map(lambda x: x[0], arr))
h = list(map(lambda x: x[1], arr))
l.sort()
h.sort()

ml = l[N // 2] if N & 1 else (l[N // 2 - 1] + l[N // 2])
mh = h[N // 2] if N & 1 else (h[N // 2 - 1] + h[N // 2])

print(mh - ml + 1)
