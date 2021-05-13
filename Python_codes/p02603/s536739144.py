import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

yen = 1000
for i in range(1, N):
    if A[i-1] < A[i]:
        yen += (A[i] - A[i-1]) * (yen // A[i-1])

print(yen)