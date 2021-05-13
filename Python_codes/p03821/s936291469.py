import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
m = map(int, read().split())
A, B = zip(*zip(m, m))

A, B = A[::-1], B[::-1]

x = 0
for a, b in zip(A, B):
    a += x
    y = (-a) % b
    x += y
print(x)