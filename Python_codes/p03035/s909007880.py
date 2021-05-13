a, b = [int(x) for x in input().split()]
print(b if a >= 13 else b // 2 if 6 <= a <= 12 else 0)