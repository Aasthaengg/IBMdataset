rpn = map(str, raw_input().split())
stack = []

for i in rpn:
    if i.isdigit():
        stack.append(i)
    else:
        n1 = int( stack.pop() )
        n2 = int( stack.pop() )

    if   i == '+':
        stack.append( str(n2+n1) )
    elif i == '-':
        stack.append( str(n2-n1) )
    elif i == '*':
        stack.append( str(n2*n1) )

print stack[0]