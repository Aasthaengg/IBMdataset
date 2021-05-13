new = input()
new_str = new.split(" ")
first = int(new_str[0])
oper = new_str[1]
last = int(new_str[2])
if oper == "+":
  print(first + last)
elif oper == "-":
  print(first - last)