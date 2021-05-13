N = int(input())
ichi = N%10
if ichi == 2 or ichi == 4 or ichi == 5 or ichi == 7 or ichi == 9:
  print("hon")
elif ichi == 3:
  print("bon")
else:
  print("pon")