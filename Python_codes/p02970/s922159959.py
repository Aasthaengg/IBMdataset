import sys
import math
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, d = map(int, readline().split())

ans = math.ceil(n / (d*2+1))

print(ans)
