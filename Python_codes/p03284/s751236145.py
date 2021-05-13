import sys
rm = lambda: map(int, sys.stdin.readline().split())

n, k = rm()
print(0 if n%k == 0 else 1)
