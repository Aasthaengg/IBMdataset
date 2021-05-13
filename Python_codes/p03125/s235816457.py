A, B = map(int, input().split())

if (A % B) == 0 or (B % A) == 0:
    print(A + B)
else:
    print(B - A)
