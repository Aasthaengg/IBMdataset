s = input()

n = len(s)
a, b = s[:(n - 1) // 2], s[(n + 1) // 2:]

print("Yes" if s == s[::-1] and a == a[::-1] and b == b[::-1] else "No")
