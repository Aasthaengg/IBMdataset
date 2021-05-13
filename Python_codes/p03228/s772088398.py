A, B, K = [int(_) for _ in input().split()]

for _ in range(K):
    B += A // 2
    A //= 2
    B, A = A, B

if K % 2 == 1:
    B, A = A, B

print(A, B)
