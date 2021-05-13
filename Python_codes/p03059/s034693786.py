import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())
a, b, t = rm()
print(int((t+0.5)//a * b))