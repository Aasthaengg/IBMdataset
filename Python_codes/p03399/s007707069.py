import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b, c, d = [int(readline()) for _ in range(4)]
print(min(a, b)+min(c, d))
