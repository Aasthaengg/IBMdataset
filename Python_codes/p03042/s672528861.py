S = input()
a = int(S[0:2])
b = int(S[2:])

if 1 <= a <= 12 and a <= b <= 12:
  print("AMBIGUOUS")
elif 1 <= a <= 12:
  print("MMYY")
elif 1 <= b <= 12:
  print("YYMM")
else:
  print("NA")