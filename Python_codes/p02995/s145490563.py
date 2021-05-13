def calc(a, b):
    x = max(a, b)
    y = min(a, b)
    while True:
        c = x % y
        if c == 0:
            break
        x = y
        y = c
    return y

A, B, C, D = map(int, input().split())

E = int(C * D / calc(C, D))
l = int(B - B // C - B // D + B // E)
m = int((A-1) - (A-1) // C - (A-1) // D + (A-1) // E)

print(l-m)