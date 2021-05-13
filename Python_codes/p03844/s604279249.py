a, op, b = input().split()
a = int(a)
b = int(b)
print(a + b * (1 if op == "+" else -1))