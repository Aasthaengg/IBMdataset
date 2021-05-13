import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c = map(int, readline().split())

print('Yes' if (a+b) >= c else 'No')