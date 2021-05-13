import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

a, b = map(int, readline().split())
if (a * b) % 2 == 0:
    print('Even')
else:
    print('Odd')
