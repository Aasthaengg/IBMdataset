import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c = map(int, readline().split())
ans = (a + b + c) - max(a, b, c)
print(ans)