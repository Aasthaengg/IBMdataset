A, B, C, K = [int(_) for _ in input().split()]

if abs(A - B) > 10 ** 18:
    print("Unfair")
else:
    if K % 2 == 0:
        print(A - B)
    else:
        print(B - A)
