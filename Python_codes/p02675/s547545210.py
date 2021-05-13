x = int(input())

l = x % 10

if l == 3:
  print("bon")
elif l == 0 or l == 1 or l == 6 or l == 8:
  print("pon")
else:
  print("hon")