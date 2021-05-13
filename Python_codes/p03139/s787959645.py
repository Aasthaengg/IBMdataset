n, a, b = [int(i) for i in input().split()]

print(min(a, b), max((a + b) - n, 0))