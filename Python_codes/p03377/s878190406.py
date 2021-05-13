import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, x = map(int, read().split())
print('YES' if a <= x <= (a+b) else 'NO')
