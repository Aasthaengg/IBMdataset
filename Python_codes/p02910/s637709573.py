li=list(input())
ll=[]
rr=[]
fl=True
for i in li:
  if fl:
    fl=False
    rr.append(i)
    continue
  fl=True
  ll.append(i)
if "L" in rr or "R" in ll:
  print("No")
else:
  print("Yes")