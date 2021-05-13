s = input()
stack = []

count = 0

for i in s:
  if not stack:
    stack.append(i)
  elif stack[-1] != i:
    stack.pop()
    count += 2
  else:
    stack.append(i)
print(count)