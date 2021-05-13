n=list(map(int,input()))
if n[0]<n[1] or (n[0]==n[1] and n[0]<n[2]):
  print(str(n[0]+1)*3)
else:
  print(str(n[0])*3)
