import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, a, b = map(int, readline().split())

print(min(n*a, b))
