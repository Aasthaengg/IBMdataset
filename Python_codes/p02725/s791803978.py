k, n, *A = map(int, open(0).read().split())
far = k + A[0] - A[-1]
for x, y in zip(A[1:], A):
    if far < x - y:
        far = x - y
print(k-far)