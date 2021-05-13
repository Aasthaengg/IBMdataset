import bisect
N, M, X = map(int, input().split())
A = list(map(int, input().split()))
t = bisect.bisect_left(A, X)
print(min(t, M-t))
