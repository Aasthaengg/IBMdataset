import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, P, *A = map(int, read().split())

A = [x & 1 for x in A]

if A.count(1):
    x = pow(2, N - 1)
else:
    x = pow(2, N)
    if P:
        x = 0
print(x)