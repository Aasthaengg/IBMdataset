import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m = map(int, readline().split())

if n == 1 and m == 1:
    print(1)
elif min(n, m) == 1 and max(n, m) >= 3:
    print(max(n, m) - 2)
else:
    print(max(n - 2, 0) * max(m - 2, 0))