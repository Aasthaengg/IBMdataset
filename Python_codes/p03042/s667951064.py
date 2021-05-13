s = input()
n1 = int(s[:2])
n2 = int(s[2:])
if 1 <= n1 <= 12 and 1 <= n2 <= 12:
  print("AMBIGUOUS")
elif (n1 > 12 or n1 == 0) and 1 <= n2 <= 12:
  print("YYMM")
elif (n2 > 12 or n2 == 0) and 1 <= n1 <= 12:
  print("MMYY")
else:
  print("NA")
