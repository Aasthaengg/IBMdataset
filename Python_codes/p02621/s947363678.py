import sys

a = int(input())
print('hello', file=sys.stderr)
print(a + a * a + a * a * a)
