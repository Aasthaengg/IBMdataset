import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, A, B = map(int, read().split())

if (A-B) & 1:
    print('Borys')
else:
    print('Alice')