inp = [int(x) for x in str(input()).split(" ")]

if inp[0] == inp[1] and inp[1] == inp[2] and inp[0] == inp[2]:
  print("Yes")
  
else:
  print("No")