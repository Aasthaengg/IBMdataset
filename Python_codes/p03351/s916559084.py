a, b, c, d = list(map(int, input().split()))

if abs(c - a) <= d or (abs(c - b) <= d and abs(b - a) <= d):
    print("Yes")
else:
    print("No")
