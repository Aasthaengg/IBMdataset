A, B = [int(_) for _ in input().split()]

if A == B:
    print(A+B)
    exit()

if A + A-1 > B + B - 1:
    print(A+A-1)
else:
    print(B+B-1)
