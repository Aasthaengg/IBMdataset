s = raw_input()
l = s.split(' ')
stk = []

for i in l:
  if i in ['+','-','*','/']:
    b = stk.pop()
    a = stk.pop()
    if i == '+':
      c = a+b
      stk.append(c)
    elif i == '-':
      c = a-b
      stk.append(c)
    elif i == '*':
      c = a * b
      stk.append(c)
    elif i == '/':
      c = a / b
      stk.append(c)
  else:
    stk.append(int(i))
print stk[0]