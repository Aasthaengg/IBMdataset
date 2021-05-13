import sys

n = int(input())

max_diff = - 10 ** 9
min_n = int(input())

for n in map(int, sys.stdin.readlines()):
  max_diff = max(max_diff, n - min_n)
  min_n = min(min_n, n)

print(max_diff)