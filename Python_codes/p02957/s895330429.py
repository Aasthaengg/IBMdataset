a, b = list(map(int, input().split()))
print((a + b) // 2 if a % 2 == b % 2 else "IMPOSSIBLE")