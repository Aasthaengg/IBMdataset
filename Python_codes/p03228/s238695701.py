A, B, K = map(int, input().split())

for i in range(K):
    if i % 2 == 0:
        # A
        if A%2 == 0:
            tmp = A//2
            A //= 2
            B += tmp
        else:
            A -= 1
            tmp = A//2
            A //= 2
            B += tmp
    else:
        # B
        if B%2 == 0:
            tmp = B//2
            B //= 2
            A += tmp
        else:
            B -= 1
            tmp = B//2
            B //= 2
            A += tmp
print(A, B)