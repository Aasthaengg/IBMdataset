A, B, C = map(int, input().split())
A, B, C = sorted([A, B, C])

if C % 2 == 0:
    print(0)
else:
    d1, d2 = C // 2, (C // 2) + 1
    e = A * B
    print(abs(d1 - d2) * e)
