S=input()
l=[]
for s in S:
  if not s in l:
    l.append(s)
if len(l) == 2:
  p = 2
  for s in S:
    if l[0] == s:
      p-=1
  if not p:
    print("Yes")
  else:
    print("No")
else:
  print("No")