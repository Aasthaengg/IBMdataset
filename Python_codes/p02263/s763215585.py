# coding: utf-8
# Here your code !
import functools
N = input().split()
stack=[]

for i in N:
    if i.isdigit():
        stack.append(int(i))
        
    else:
        key=0
        if i=="+":
            p2=stack.pop()
            p1=stack.pop()
            stack.append(p1+p2)
        elif i=="-":
            p2=stack.pop()
            p1=stack.pop()
            stack.append(p1-p2)
        elif i=="*":
            p2=stack.pop()
            p1=stack.pop()
            stack.append(p1*p2)
print(stack[0])