A, B = list(map(int, input().split()))

calc = []
calc.append(A + B)
calc.append(A - B)
calc.append(A * B)

print(max(calc))