s = input()
f,b = int(s[:2]),int(s[2:])
if 1 <= f <= 12:
  if 1 <= b <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1 <= b <= 12:
    print("YYMM")
  else:
    print("NA")