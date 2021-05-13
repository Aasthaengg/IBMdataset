import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

n, *a = map(int, read().split())
ans = float('inf')
for i in (-1, 1):
    cnt, now = 0, 0
    for aa in a:
        now += aa
        if now * i <= 0:
            cnt += abs(now - i)
            now = i
        i *= -1
    ans = min(ans, cnt)
print(ans)
