N = int(input())
a = N // 100
b = N % 100
if 1 <= a <= 12:
  if 1 <= b <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1 <= b <= 12:
    print("YYMM")
  else:
    print("NA")