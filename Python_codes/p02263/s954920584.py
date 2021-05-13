#input
char_list = raw_input().split()

#calculation
stack = []
for x in char_list:
    if x == "+":
        a = stack.pop()
        b = stack.pop()
        stack.append(a+b)
    elif x=="-":
        a = stack.pop()
        b = stack.pop()
        stack.append(b-a)
    elif x=="*":
        a = stack.pop()
        b = stack.pop()
        stack.append(a*b)
    else:
        stack.append(int(x))

#output
print stack[0]