input_ = raw_input().split()

stack = []
for s in input_:
    if s.isdigit():
        stack.append(s)
    else:
        x = stack.pop()
        y = stack.pop()
        ans = eval(y + s + x)
        stack.append(str(ans))
        
print stack[0]