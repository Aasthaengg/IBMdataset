A, B, K = map(int, input().split())

for i in range(K):
    if i % 2 == 0:
        if A % 2 != 0:
            A -= 1
        num = A // 2
        A = num
        B += num
    else:
        if B % 2 != 0:
            B -= 1
        num = B // 2
        B = num
        A += num

print(A, B)