import sys
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, a, b, c = map(int, readline().split())
l = [int(readline()) for _ in range(n)]

ans = float('inf')
for pattern in itertools.product(range(4), repeat=n):
    cnt = [0] * 4
    length = [0] * 4
    mp = 0
    for i, v in enumerate(pattern):
        if cnt[v] != 0 and 0 <= v <= 2:
            mp += 10
        cnt[v] += 1
        length[v] += l[i]
    if cnt[0] > 0 and cnt[1] > 0 and cnt[2] > 0:
        mp += abs(a - length[0]) + abs(b - length[1]) + abs(c - length[2])
        ans = min(ans, mp)

print(ans)