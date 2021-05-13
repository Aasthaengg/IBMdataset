a, b, c = map(int, input().split())
y = -(-a // 2) * b * c
print(min(a * b, b * c, c * a) if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 else 0)