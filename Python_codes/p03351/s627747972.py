a, b, c, d = map(int, input().split())
print('Yes' if abs(a - c) <= d or abs(a - b) + abs(b - c) < 2*d else 'No')