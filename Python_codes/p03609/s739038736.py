import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, t = map(int, readline().split())
print(max(0, x-t))