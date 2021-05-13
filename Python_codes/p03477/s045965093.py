a, s, d, f = map(int, input().split())
if a + s > d + f:
    print("Left")
elif a + s == d + f:
    print("Balanced")
else:
    print("Right")
