import bisect

n = int(input())
A = [int(_) for _ in input().split()]

A.sort()
x = A[-1]
y = bisect.bisect(A, x / 2)

if abs(A[y] - x / 2) < abs(A[y-1] - x / 2):
    print(x, A[y])
else:
    print(x, A[y-1])
