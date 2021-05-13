N = int(input())
A = []
B = []
for n in range(N):
    a, b = [int(n) for n in input().split()]
    A.append(a)
    B.append(b)

A.sort()
B.sort()

if N % 2 == 0:
    median_max = B[N//2-1] + B[N//2]
    median_min = A[N//2-1] + A[N//2]
    print(median_max - median_min + 1)
else:
    print(B[N//2] - A[N//2] + 1)
