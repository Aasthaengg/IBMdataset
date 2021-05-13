import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a, *b = map(int, read().split())

ans = sum(b) - max(b) // 2
print(ans)
