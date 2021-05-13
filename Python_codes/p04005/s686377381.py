A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)
else:
    a = abs((A // 2) * B * C - ((A + 1) // 2) * B * C)
    b = abs(A * (B // 2) * C - A * ((B + 1) // 2) * C)
    c = abs(A * B * (C // 2) - A * B * ((C + 1) // 2))
    print(min(a, b, c))
