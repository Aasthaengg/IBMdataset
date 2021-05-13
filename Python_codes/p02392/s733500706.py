inputStr = raw_input().split(' ')
a = int(inputStr[0])
b = int(inputStr[1])
c = int(inputStr[2])
if a < b & b < c:
  print("Yes")
else:
  print("No")