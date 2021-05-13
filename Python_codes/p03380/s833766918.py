from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))
A.sort()
if N == 2:
    print(A[1], A[0])
    exit()
a = A[-1]
k = bisect_left(A, a/2)
x = a/2-A[k-1]
y = A[k]-a/2
if x <= y:
    b = A[k-1]
else:
    b = A[k]
print(a, b)
