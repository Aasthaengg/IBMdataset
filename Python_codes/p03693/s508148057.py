print("NO" if sum([int(x)*int(y) for x, y in zip(input().split(), [100, 10, 1])])%4 else "YES")