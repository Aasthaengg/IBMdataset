import sys
rm = lambda: map(int, sys.stdin.buffer.readline().split())

a, b = rm()
print(a+b if b%a == 0 else b-a)
