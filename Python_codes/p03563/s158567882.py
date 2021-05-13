import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

r, g = [int(readline()) for _ in range(2)]
ans = r + (g - r) * 2
print(ans)