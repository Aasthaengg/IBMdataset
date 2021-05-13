#ABC168-A
num = int(input()) % 10
if num == 3:
  print("bon")
elif num == 8 or num == 6 or num <= 1:
  print("pon")
else:
  print("hon")