import sys, operator

list = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

for line in sys.stdin:
    a, op, b = line.split()
    if op == '?': break
    print(int(list[op](int(a), int(b))))