import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

k = int(readline())
print((k // 2) ** 2 if k % 2 == 0 else ((k // 2)*(k // 2+1)))
