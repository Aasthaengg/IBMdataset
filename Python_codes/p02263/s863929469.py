equ = input().split()

stack = []


def push(x, stack):
    stack.append(x)
    return stack
def pop(stack):
    val = stack.pop()
    return val,stack

for symbol in equ:
    if symbol.isnumeric():
        stack = push(int(symbol),stack)
    else:
        val1, stack = pop(stack)
        val2, stack = pop(stack)
        if symbol == '+':
            stack = push(val1+val2, stack)
        elif symbol == '-':
            stack = push(val2-val1, stack)
        elif symbol == '*':
            stack = push(val1*val2, stack)

print(stack[0])
