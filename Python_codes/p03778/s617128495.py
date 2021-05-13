
x, a, b = map(int, input().split())

print(a - (b + x) if a > b else max(0, b - (a + x)))