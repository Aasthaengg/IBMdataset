import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, m, x, *a = map(int, read().split())
left_cost = len([i for i in a if 0 < i < x])
right_cost = len([i for i in a if x < i < n])

print(min(left_cost, right_cost))
