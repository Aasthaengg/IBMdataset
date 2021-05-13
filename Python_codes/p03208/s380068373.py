import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k, *h = map(int, read().split())

h.sort()
ans = 10 ** 9
for i in range(n - k + 1):
    ans = min(ans, h[i + k - 1] - h[i])
print(ans)