import math
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, k, *a = map(int, readline().split())

ans = math.ceil((n-1)/(k-1))
print(ans)