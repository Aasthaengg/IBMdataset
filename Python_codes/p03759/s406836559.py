a, b, c = map(int, input().split())
print('YES' if (max(a, b, c) + min(a, b, c)) / 2 == (a + b + c) / 3 else 'NO')