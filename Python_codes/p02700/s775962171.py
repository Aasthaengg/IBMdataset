a, b, c, d = map(int, input().split())

while c or a >= 0:
    c -= b
    a -= d
    if c <= 0:
        print("Yes")
        break
    if a <= 0:
        print("No")
        break