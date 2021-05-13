import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
a = [list(map(int, readline().split())) for _ in range(2)]

ans = 0
for i in range(n):
    ans = max(ans, sum(a[0][:i + 1:]) + sum(a[1][i::]))
print(ans)