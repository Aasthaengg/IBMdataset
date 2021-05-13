N = int(input())
A = [int(x) for x in input().split()]

def op(x, y):
    print(x, y)
    A[y - 1] += A[x - 1]

mn, mx = min(A), max(A)
base = mx if abs(mn) < abs(mx) else mn
bi = A.index(base) + 1

print(N * 2 - 1)
for i in range(N):
    op(bi, i + 1)
if 0 < base:
    for i in range(1, N):
        op(i, i+1)
else:
    for i in range(N, 1, -1):
        op(i, i-1)