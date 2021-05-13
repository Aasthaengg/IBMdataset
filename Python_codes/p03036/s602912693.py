import sys
input = sys.stdin.readline
r, D, x = map(int, input().split())
for _ in range(1, 11):
  print(r * x - D)
  x = r * x - D