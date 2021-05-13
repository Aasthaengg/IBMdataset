s = input()
x = int(s) // 100
y = int(s) % 100
if 1 <= x <= 12:
  if 1 <= y <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1 <= y <= 12:
    print("YYMM")
  else:
    print("NA")