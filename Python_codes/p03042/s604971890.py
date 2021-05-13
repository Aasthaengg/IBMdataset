S =int(input())
a = S // 100
b = S % 100
if 0 < a < 13 :
  if 0 < b < 13:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 0 < b < 13:
    print("YYMM")
  else:
    print("NA")