s = input()
s = s.split()
num1 = int(s[0])
op = s[1]
num2 = int(s[2])

if op == "+":
  print(num1+num2)
else:
  print(num1-num2)