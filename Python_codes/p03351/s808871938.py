a, b, c, d = map(int, input().split())
if abs(a - c) <= d:
    print("Yes")
elif ((a <= b and b <= c) or (c <= b and b <= a)) and abs(a - b) <= d and abs(b - c) <= d:
    print("Yes")
else:
    print("No")