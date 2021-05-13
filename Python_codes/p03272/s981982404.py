import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())

a, b = rm()
print(a-b+1)