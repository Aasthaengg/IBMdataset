stack = []
for i in input().split():
  if i in ['+', '-', '*']:
    b, a = stack.pop(), stack.pop()
    if i == '+': stack.append(a + b)
    if i == '-': stack.append(a - b)
    if i == '*': stack.append(a * b)
  else:
    stack.append(int(i))
print(stack.pop())