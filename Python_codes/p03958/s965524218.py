K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
print(max(A[-1]-sum(A[:-1])-1, 0))