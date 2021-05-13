import sys
a, b, t = map(int, sys.stdin.buffer.readline().split())
print(int((t+0.5)//a * b))
