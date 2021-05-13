import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())
a, b, c = rm()
print(min(c, b//a))