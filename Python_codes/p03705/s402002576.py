import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, A, B = map(int, read().split())

if A > B:
    x = 0
elif N == 1:
    x = 1 * (A == B)
else:
    low = A * (N - 1) + B
    high = B * (N - 1) + A
    x = high - low + 1
print(x)