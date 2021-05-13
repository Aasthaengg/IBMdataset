print((lambda a, b: b if a > 12 else b // 2 if a > 5 else 0)(*map(int, input().split())))
