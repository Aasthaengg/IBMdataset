n = int(input())
print("Yes" if any([n == 4 * x + 7 * y for x in range(n // 4 + 1) for y in range(n // 7 + 1)]) else "No")