import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d = map(int, read().split())
if abs(a - c) <= d:
    print('Yes')
elif abs(a - b) <= d and abs(b - c) <= d:
    print('Yes')
else:
    print('No')
