def eat(a, b):
    e = A[a] + A[b] - X
    if 0 < e <= A[b]:
        A[b] -= e
    elif e > A[b]:
        e -= A[b]
        A[b] = 0
        A[a] -= e

N, X = map(int, input().split())
A = list(map(int, input().split()))
before_eat = sum(A)
eat(-1, -2)
for i in range(N - 1):
    eat(i, i + 1)
print(before_eat - sum(A))