l = list(input())

if ("C" in l) & ("F" in l):
  if min([i for i, x in enumerate(l) if x == 'C']) < max([i for i, x in enumerate(l) if x == 'F']):
  	print("Yes")
  else:
    print("No")
else:
  print("No")
