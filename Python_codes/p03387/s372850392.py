A, B, C = map(int, input().split())

X = max([A, B, C])
X = X if (3 * X - (A + B + C)) % 2 == 0 else X + 1
diff = 3 * X - (A + B + C)

print(diff // 2)
