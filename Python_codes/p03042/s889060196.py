s = int(input())
a = s % 100
b = ((s-a) / 100)
if a <= 12 and b <= 12 and a != 0 and b != 0:
  print("AMBIGUOUS")
elif b <= 12 and b != 0:
  print("MMYY")
elif a <= 12 and a != 0:
  print("YYMM")
else:
  print("NA")