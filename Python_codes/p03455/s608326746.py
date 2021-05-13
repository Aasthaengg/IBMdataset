textLine = input().split()
num1 = int(textLine[0])
num2 = int(textLine[1])
if num1 * num2 % 2 == 0:
  print("Even")
else:
  print("Odd")