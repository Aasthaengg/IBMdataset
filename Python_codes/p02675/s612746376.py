n = int(input())
a = n-(n//100)*100
b = a-(a//10)*10
if b == 2 or b == 4 or b == 5 or b == 7 or b == 9:
  print("hon")
if b == 0 or b == 1 or b == 6 or b == 8:
  print("pon")
if b == 3:
  print("bon")

