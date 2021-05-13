x = [int(_) for _ in input().split()]
print('A' if abs(x[1] - x[0]) < abs(x[2] - x[0]) else 'B')