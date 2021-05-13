def add(a, b):
    return b+a
def sub(a, b):
    return b-a
def mul(a, b):
    return b*a
def div(a, b):
    if a!=0:
        return b/a
    else:
        return 10000
operators = {'+':add, '-':sub, '*':mul, '/':div}

def calc_PRN(symbols):
    stack = []
    for s in symbols:
        if s in operators.keys():
            stack.append(operators[s](stack.pop(), stack.pop()))
        else:
            stack.append(int(s))
    return stack[-1]


if __name__ == '__main__':
    symbols = input().split()
    print(int(calc_PRN(symbols)))