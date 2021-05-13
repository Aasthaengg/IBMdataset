a, b = [int(i) for i in input().split()]
a, b = [a, b] if a < b else [b, a]
print(str(a) * b)