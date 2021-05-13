import math
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *l = map(int, read().split())

cost = math.ceil(n / min(l))
cost += 4

print(cost)