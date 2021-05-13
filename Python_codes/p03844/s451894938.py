a = input()
b = a.split()
first = int(b[0])
op = b[1]
second = int(b[2])

if(op == "-"):
  print(first-second)
elif(op == "+"):
  print(first + second)

