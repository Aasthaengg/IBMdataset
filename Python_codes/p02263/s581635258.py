def cal(ope,a,b):
    if ope=="+":
        x=a+b
    elif ope=="-":
        x=a-b
    elif ope=="*":
        x=a*b
    return x

lst=input().split()
stack=[]
for i in range(len(lst)):
    if lst[i]=="+" or lst[i]=="-" or lst[i]=="*": pass
    else:
        lst[i]=int(lst[i])
for i in range(len(lst)):
    if lst[i]=="+" or lst[i]=="-" or lst[i]=="*": 
        a=stack.pop()
        b=stack.pop()
        c=cal(lst[i],b,a)
        stack.append(c)
    else:
        stack.append(lst[i])
print(stack[0])
