operand = []
for x in raw_input().split():
  if x.isdigit():
    operand.append(int(x))
  else:
    a1 = operand.pop()
    a2 = operand.pop()
    if  x == '+' :
      operand.append(a2 + a1)
    elif  x == '-':
      operand.append(a2 - a1)
    elif  x == '*':
      operand.append(a2 * a1)

print operand.pop()