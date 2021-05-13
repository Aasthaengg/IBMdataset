import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *h = map(int, read().split())

ans = h[0]
for i in range(1,n):
    if h[i] > h[i-1]:
        ans += (h[i]-h[i-1])

print(ans)