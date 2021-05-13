import sys
read = sys.stdin.read

A, B, K = map(int, read().split())

for i in range(K):
    if i % 2 == 0:
        A //= 2
        B += A
    else:
        B //= 2
        A += B

print(A, B)