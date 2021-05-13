import sys

for line in sys.stdin:
  items = line.strip().split()

stack = []

for item in items:
  if item == '+' or item == '-' or item == '*':
    x = stack.pop()
    y = stack.pop()
    exp = "%s %s %s" % (y, item, x)
    stack.append(eval(exp))
  else:
    stack.append(int(item))

print stack.pop()