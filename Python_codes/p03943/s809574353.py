a, b, c = map(int, input().split())
print((a + b == c or a + c == b or b + c == a) and "Yes" or "No")