import sys

n, *a = map(int, sys.stdin.read().split())
print('second' if all(x % 2 == 0 for x in a) else 'first')
