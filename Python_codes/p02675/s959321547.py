N = int(input())
x = N%10
Lpon = [0,1,6,8]

if x == 3:
  print("bon")
elif x in Lpon:
  print("pon")
else:
  print("hon")