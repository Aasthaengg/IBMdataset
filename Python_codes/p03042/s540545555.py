S = input()
a = S[0:2]
b = S[2:4]
A = int(a)
B = int(b)
if A>=1 and A <=12:
  if B>= 1 and B <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if B>= 1 and B<= 12:
    print("YYMM")
  else:
    print("NA")