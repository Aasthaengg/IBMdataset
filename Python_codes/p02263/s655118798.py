def main():
  inps = list(input().split(" "))
  # print(inps)

  stack = []
  for inp in inps:
    if inp == "+":
      a = int(stack.pop(-2))
      b = int(stack.pop(-1))
      stack.append(a+b)
    elif inp == "-":
      a = int(stack.pop(-2))
      b = int(stack.pop(-1))
      stack.append(a-b)
    elif inp == "*":
      a = int(stack.pop(-2))
      b = int(stack.pop(-1))
      stack.append(a*b)
    else:
      stack.append(inp)
    # print(inp, type(inp), stack)
  print(int(stack[0]))

main()
