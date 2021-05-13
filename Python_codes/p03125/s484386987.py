A, B = map(int, input().split())

if divmod(B, A)[1] == 0:
    print(A + B)
else:
    print(B - A)
