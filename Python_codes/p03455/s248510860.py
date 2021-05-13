input = input("")
input = input.split()

if int(input[0]) * int(input[1]) % 2 == 0:
  print("Even")
else:
  print("Odd")