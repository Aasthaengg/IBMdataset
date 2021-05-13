A, B, K = map(int, input().split())

cnt = 0
for i in range(K):
    if i % 2 == 0:
        if A % 2 != 0:
            A = (A-1) // 2
        else:
            A //= 2
        B += A

    else:
        if B % 2 != 0:
            B = (B-1) // 2
        else:
            B //= 2
        A += B

    cnt += 1

print(A, B)
