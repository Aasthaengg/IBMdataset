a, b = map(int, input().rstrip().split())
b2 = b * 2
r = 0 if a <= b2 else a - b2
print(r)
