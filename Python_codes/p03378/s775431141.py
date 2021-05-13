from bisect import bisect_left

N, M, X = list(map(int, input().split()))
A = [int(X) for X in input().split()]

i = bisect_left(A, X)
print(min(i, len(A) - i))