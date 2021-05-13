n, x, *A = map(int, open(0).read().split())
s = 0
if A[0] > x:
    s += A[0] - x
    A[0] = x
for i in range(1, n):
    if A[i] + A[i-1] > x:
        s += A[i] + A[i-1] - x
        A[i] = x - A[i-1]
print(s)