import sys
import itertools
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


n = int(readline())
fs = [list(map(int, readline().split())) for _ in range(n)]
ps = [list(map(int, readline().split())) for _ in range(n)]

pat = list(itertools.product([0, 1], repeat=10))

ans = -10**9
for p in pat:
    if sum(list(p)) == 0:
        continue
    money = 0
    for i in range(n):
        cnt = 0
        for j in range(10):
            if fs[i][j] == 1 and p[j] == 1:
                cnt += 1
        money += ps[i][cnt]
    if ans < money:
        ans = max(ans, money)
print(ans)