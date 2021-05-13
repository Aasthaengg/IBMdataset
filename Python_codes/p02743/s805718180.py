a, b, c = map(int, input().split())
s, t = a + b, a * b
print("Yes" if c - s > 0 and (c - s) ** 2 - 4 * t > 0 else "No")