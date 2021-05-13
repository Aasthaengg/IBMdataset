A,B=map(str,input().split())
if A=="H" and B=="H":
  print("H")
elif A=="H" and B=="D":
  print("D")
elif A=="D" and B=="H":
  print("D")
else:
  print("H")