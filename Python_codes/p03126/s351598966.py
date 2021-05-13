n, m = map(int, input().split())

X = {i for i in range(1, m+1)}
for i in range(n):
    k, *A = map(int, input().split())
    X = X & set(A)
print(len(X))