import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, y = map(int, readline().split())

l = []
while x <= y:
    l.append(x)
    x *= 2

print(len(l))