N = int(input())
A = [int(x) for x in input().split()]

mn, mx = min(A), max(A)

def op(x, y):
    print(x, y)
    print(x, y)
    A[y - 1] += A[x - 1]
    A[y - 1] += A[x - 1]

print(N * 2)
if abs(mn) < abs(mx):
    base = mx
    bi = A.index(base) + 1
    op(bi, 1)
    for i in range(N-1):
        op(i+1, i+2)
else:
    base = mn
    bi = A.index(base) + 1
    op(bi, N)
    for i in range(N, 1, -1):
        op(i, i-1)
