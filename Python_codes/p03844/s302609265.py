inputs = list(input().split())
a, op, b = int(inputs[0]), inputs[1], int(inputs[2])

print(a + b if op == '+' else a - b)