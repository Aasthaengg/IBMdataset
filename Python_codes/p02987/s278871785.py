from collections import defaultdict
s = str(input())
d = defaultdict(int)
for x in s:
  d[x]+=1
if len(d)==2:
  for key in d:
    if d[key]!=2:
      print("No")
      exit()
  print("Yes")
else:
  print("No")
  
