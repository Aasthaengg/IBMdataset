a, b, c, d = map(int, input().split())
if a+b == c+d:
    print("Balanced")
    exit()
if a+b > c+d:
    print("Left")
    exit()
if a+b < c+d:
    print("Right")
    exit()
