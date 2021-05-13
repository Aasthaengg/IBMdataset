X = input()
N = len(X)
stack = []
for x in X:
  if x == "S":
    stack.append(x)
  else:
    if len(stack) == 0 or stack[-1] == "T":
      stack.append(x)
    else:
      stack.pop()
      
print(len(stack))