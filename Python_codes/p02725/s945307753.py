import sys
read = sys.stdin.buffer.read
k, n, *A = map(int, read().split())
far = k + A[0] - A[-1]
y = A[0]
for x in A:
    if far < x - y:
        far = x - y
    y = x
print(k-far)