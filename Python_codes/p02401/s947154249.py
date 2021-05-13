a_list = []
b_list = []
op_list = []
count = 0
while True:
  a, op, b = (str(i) for i in input().split())
  if op != '?':
    a_list.append(int(a))
    b_list.append(int(b))
    op_list.append(op)
    count += 1
  else :
    break
for i in range(0,count):
  if op_list[i] == '+':
    print(a_list[i] + b_list[i])
  elif op_list[i] == '-':
    print(a_list[i] - b_list[i])
  elif op_list[i] == '*':
    print(a_list[i] * b_list[i])
  elif op_list[i] == '/':
    print(a_list[i] // b_list[i])