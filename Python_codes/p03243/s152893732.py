import bisect

N = int(input())
A = [111, 222, 333, 444, 555, 666, 777, 888, 999]

print(A[bisect.bisect_left(A, N)])
