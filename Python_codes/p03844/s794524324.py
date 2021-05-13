def ope(ope, a, b):
    if ope == '+':
        return a+b
    
    elif ope == '-':
        return a-b

a, op, b = map(str, input().split())

print(ope(op, int(a), int(b)))