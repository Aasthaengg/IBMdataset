import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def f(A, B, C):
    for _ in range(3):
        A, B, C = B, C, A
        if A % 2 == 0:
            yield 0
        yield B * C

A, B, C = map(int, read().split())
print(min(f(A, B, C)))