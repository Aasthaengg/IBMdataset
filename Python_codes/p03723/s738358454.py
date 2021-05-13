import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

A, B, C = map(int, read().split())

for t in range(1000):
    if A & 1 or B & 1 or C & 1:
        break
    A, B, C = A // 2, B // 2, C // 2
    A, B, C = B + C, C + A, A + B

t = -1 if t > 100 else t
print(t)