S = input()
L, R =  map(int, [S[:2], S[2:]])
 
if 1 <= L <= 12 and 1 <= R <= 12:
  print("AMBIGUOUS")
elif 1 <= L <= 12 and (R == 0 or R > 12):
  print("MMYY")
elif (L == 0 or L > 12) and 1 <= R <= 12:
  print("YYMM")
else:
  print("NA")