A, B, C = map(int, input().split())
if C - B - A <= 0:
    print(C + B)
elif C - B == A:
    print(2 * B + A)
else:
    print(2 * B + A + 1)
