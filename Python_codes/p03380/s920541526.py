n = int(input())
A = map(int, input().split())
A = sorted(A)
maxa = max(A)

from bisect import bisect_left
m = (maxa+1)//2
l2 = bisect_left(A, m)

if abs(A[l2] - m) >= abs(A[l2-1] - m):
    print(maxa, A[l2-1])
else:
    print(maxa, A[l2])

