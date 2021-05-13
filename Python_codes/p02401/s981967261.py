import sys

for line in sys.stdin:

    a_str, op, b_str = line.split()

    if op == '?': break
    
    a, b = int(a_str), int(b_str)

    if op == '+':
        print a + b
    elif op == '-':
        print a - b
    elif op == '*':
        print a * b
    elif op == '/':
        print a / b