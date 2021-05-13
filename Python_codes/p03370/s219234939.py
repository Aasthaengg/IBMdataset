N, X = map(int, input().split())
A = list()
for i in range(N):
    A.append(int(input()))

A.sort()

print((X - sum(A)) // A[0] + N)