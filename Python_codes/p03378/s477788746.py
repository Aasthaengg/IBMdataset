N, M, X = map(int, input().split())
A = [int(a) for a in input().split()]

A.append(X)
A = sorted(A)

lst = [len(A[:A.index(X)]), len(A[A.index(X)+1:])]

print(min(lst))