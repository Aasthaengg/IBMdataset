def m(s):
  return True if 1 <= int(s) <= 12 else False

s = input()
f = int(s[:2])
l = int(s[2:])

if m(f) and m(l):
  print("AMBIGUOUS")
elif m(f):
  print("MMYY")
elif m(l):
  print("YYMM")
else:
  print("NA")

