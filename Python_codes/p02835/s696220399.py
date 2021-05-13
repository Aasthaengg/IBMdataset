a = input().split()
b = [int(s) for s in a]
if sum(b) > 21:
  print("bust")
else:
  print("win")