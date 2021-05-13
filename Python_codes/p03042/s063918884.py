S = input()
l, r =  map(int, [S[:2], S[2:]])

if 1 <= l <= 12 and 1 <= r <= 12:
  print("AMBIGUOUS")
elif 1 <= l <= 12 and (r == 0 or r > 12):
  print("MMYY")
elif (l == 0 or l > 12) and 1 <= r <= 12:
  print("YYMM")
else:
  print("NA")