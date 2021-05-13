import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x1, y1, x2, y2 = map(int, readline().split())

a = x2 - x1
b = y2 - y1
x3, y3 = x2 - b, y2 + a
x4, y4 = x1 - b, y1 + a

print(x3, y3, x4, y4)
