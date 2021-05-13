import sys

a, b = map(int, next(sys.stdin.buffer).split())
if a > b:
    a, b = b, a
print(str(a) * b)
