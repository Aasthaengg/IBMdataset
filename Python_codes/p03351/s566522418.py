a, b, c, d = map(int, input().split())
print("Yes" if abs(a - c) <= d or abs(a - b) <= d >= abs(b - c) else "No")
