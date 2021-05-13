X = input()
num_t = 0
stack = []
for x in X:
  if x == 'S':
    stack.append(x)
  else:
    if stack:
      stack.pop()
    else:
      num_t += 1

print(num_t + len(stack))