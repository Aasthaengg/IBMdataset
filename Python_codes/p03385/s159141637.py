a = str(input())
s = set()
for x in a:
  s.add(x)
if len(s)==3:
  print("Yes")
else:
  print("No")