import bisect
import sys

N, H = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
a, b = [list(i) for i in zip(*ab)]

a_max = max(a)
b.sort(reverse=True)

l = [b[i] for i in range(N) if b[i] >= a_max]
d = 0
cnt = 0
for v in l:
    d += v
    cnt += 1
    if d >= H:
        print(cnt)
        sys.exit()
cnt += (H-d+a_max-1)//a_max
print(cnt)