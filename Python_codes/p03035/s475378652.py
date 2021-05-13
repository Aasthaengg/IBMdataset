a, b = map(int, input().split())
if a < 6:
    print(0)
else:
    print(b if a > 12 else b // 2)
