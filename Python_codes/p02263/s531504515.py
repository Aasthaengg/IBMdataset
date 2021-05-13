data = list(map(str,input().split()))
stack = []
op1 = 0
op2 = 0
k = 0
for i in data:
# print(i,type(i))
  if(i == "+" or i == "-" or i == "*" or i == "/"):
    op1 = stack.pop()
    op2 = stack.pop()
    if(i == "+"): stack.append(op2+op1)
    elif(i == "-"): stack.append(op2-op1)
    elif(i == "*"): stack.append(op2*op1)
    elif(i == "/"): stack.append(int(op2/op1))
  else:
    stack.append(int(i))


print(stack.pop())

