import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, a, b = [int(readline()) for _ in range(3)]
print((x-a) % b)