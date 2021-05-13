import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, *A = map(int, read().split())

def f(A):
    low, high = 2, 2
    for x in A[::-1]:
        low += (-low) % x
        high -= (high) % x
        if low > high:
            print(-1)
            return
        low, high = low, high+(x-1)
    print(low, high)

f(A)