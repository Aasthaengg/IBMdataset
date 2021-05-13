X = int(input())
r = 0 if (X % 11) % 6 == 0 else 1
print((X // 11) * 2 + (X % 11) // 6 + r)