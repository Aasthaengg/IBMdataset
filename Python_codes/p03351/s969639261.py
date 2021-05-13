a,b,c,D=[int(s) for s in input().split()]
if abs(c-a)<=D:
  print("Yes")
elif abs(b-a)<=D and abs(c-b)<=D:
  print("Yes")
else:
  print("No")