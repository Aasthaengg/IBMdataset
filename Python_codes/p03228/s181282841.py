A, B, K = map(int,input().split())

for _ in range(K // 2):
    A //= 2
    B += A
    B //= 2
    A += B
if K % 2 == 1:
    A //= 2
    B += A

print(str(A), end=" ")
print(str(B))