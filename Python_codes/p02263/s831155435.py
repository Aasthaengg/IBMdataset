args = input().split()
stack = []

def cal_with_operator(b, a, operator):
    return eval('{} {} {}'.format(a, operator, b))

for s in args:
    if s == '+': stack.append(cal_with_operator(stack.pop(), stack.pop(), '+'))
    elif s == '-': stack.append(cal_with_operator(stack.pop(), stack.pop(), '-'))
    elif s == '*': stack.append(cal_with_operator(stack.pop(), stack.pop(), '*'))
    elif s == '/': stack.append(cal_with_operator(stack.pop(), stack.pop(), '/'))
    else : stack.append(s)

print(stack[0])
