n = int(input())
A = list(map(int, input().split()))

A.sort()

m = A[-1]
M = [abs((m / 2) - a) for a in A[: -1]]
r = A[M.index(min(M))]

print(m, r)
