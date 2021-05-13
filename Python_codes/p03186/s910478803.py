A, B, C = tuple(map(int, input().split()))
if (A + B) < C:
    print(A + 2 * B + 1)
else:
    print(B + C)