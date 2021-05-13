A, B, K = map(int, input().split())
for i in range(K):
    if i % 2 == 0:
        half = A // 2
        A, B = half, B + half
    else:
        half = B // 2
        A, B = A + half, half
print(A, B)