l=list(input().split())
l=l[::-1]
stack=[]
while len(l)>0:
  n=l.pop()
  if n in ["+","-","*"]:
    a=int(stack.pop())
    b=int(stack.pop())
    if n=="+":
      stack.append(a+b)
    elif n=="-":
      stack.append(b-a)
    else:
      stack.append(a*b)
  else:
    stack.append(n)
print(stack[-1])
