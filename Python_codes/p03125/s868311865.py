import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())

a, b = rm()
print(b-a if b%a else a+b)