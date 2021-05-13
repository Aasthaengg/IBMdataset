import sys

K, T = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))

if len(A) == 1:
    print(A[0] - 1)
else:    
    A.sort(reverse=True)
    other_sum = sum(A[1:])
    print(max(0, A[0] - other_sum - 1))