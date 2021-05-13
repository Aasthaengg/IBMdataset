import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, a = [int(readline()) for _ in range(2)]
print(n**2 - a)