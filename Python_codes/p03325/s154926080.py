import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *a = map(int, read().split())

ans = 0
for x in a:
    while x % 2 == 0:
        x = x // 2
        ans += 1

print(ans)