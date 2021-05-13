import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())

a, b = rm()
c, d = rm()
print((c-a) * (d-b))













