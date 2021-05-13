def resolve():
    A, B, K = map(int, input().split())
    if K%2 == 0:
        for i in range(K//2):
            if A%2 == 1:
                A -= 1
            B += A//2
            A -= A//2
            if B%2 == 1:
                B -= 1
            A += B//2
            B -= B//2
    else:
        for i in range(K//2):
            if A%2 == 1:
                A -= 1
            B += A//2
            A -= A//2
            if B%2 == 1:
                B -= 1
            A += B//2
            B -= B//2
        if A % 2 == 1:
            A -= 1
        B += A // 2
        A -= A // 2
    print(A, B)
resolve()