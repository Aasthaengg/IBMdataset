books = int(input())
b1 = books % 10
if b1 in (2,4,5,7,9):
  print("hon")
elif b1 in (0,1,6,8):
  print("pon")
else:
  print("bon")