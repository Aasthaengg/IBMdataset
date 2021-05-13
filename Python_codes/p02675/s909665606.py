N = str(input())

if N[-1] is "3":
  print("bon")
elif N[-1] is "0" or N[-1] is "1" or N[-1] is "6" or N[-1] is "8":
  print("pon")
else:
  print("hon")