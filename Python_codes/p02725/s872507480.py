import sys
read = sys.stdin.buffer.read
k, n, *A = map(int, read().split())
A += [A[0] + k]
far = max(y - x for x, y in zip(A, A[1:]))
print(k - far)