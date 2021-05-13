import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())
ab = [list(map(int, readline().split())) for _ in range(n)]

ab.sort()

cnt = 0
ans = 0
for a, b in ab:
    if cnt + b < m:
        cnt += b
        ans += b * a
    else:
        ans += (m - cnt) * a
        break
print(ans)