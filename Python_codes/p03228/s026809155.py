A, B, K = map(int, input().split())

takahasi = True
for _ in range(K):
    if takahasi is True:
        A //= 2
        B += A
    else:
        B //= 2
        A += B
    takahasi = not takahasi

print(A, B)
