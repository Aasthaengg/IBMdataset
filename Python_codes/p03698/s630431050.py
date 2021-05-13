s=input()
n=len(s)
d=set()
for ss in s:
  d.add(ss)
if len(d)==n:
  print("yes")
else:
  print("no")