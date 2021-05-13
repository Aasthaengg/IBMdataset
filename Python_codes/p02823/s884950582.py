N, A, B = map(int, input().split())

ab = B - A

if ab % 2 == 1:
    print(min(A - 1, N - B) + 1 + (B - A - 1) // 2)
else:
    print(abs((A + B) // 2 - A))
