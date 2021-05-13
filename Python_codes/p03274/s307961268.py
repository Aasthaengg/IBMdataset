import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k, *x = map(int, read().split())

ans = float('inf')
for i in range(n - k + 1):
    right = x[i + k - 1]
    left = x[i]
    if right <= 0:
        time = abs(left)
    elif left <= 0 < right:
        time = abs(right-left)
        time += min(abs(right), abs(left))
    elif 0 < left:
        time = abs(right)
    ans = min(ans, time)
print(ans)
