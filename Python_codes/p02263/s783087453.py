def r_poland(s):
    stack=[]
    
    for d in s:
        if d.isdigit():
            stack.append(int(d))
        elif d=="+":
            stack[-1]+=stack.pop(-2)
        elif d=="-":
            stack[-1]=stack.pop(-2)-stack[-1]
        elif d=="*":
            stack[-1]*=stack.pop(-2)

    return stack
   
s=list(input().split())

print(*r_poland(s))