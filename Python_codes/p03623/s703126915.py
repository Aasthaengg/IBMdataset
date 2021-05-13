import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, a, b = map(int, readline().split())
if abs(x - a) < abs(x - b):
    print('A')
else:
    print('B')