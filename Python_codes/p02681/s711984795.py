import re
s=str(input())
t=str(input())
for i in range(len(s)):
 if s[i]!=t[i]:
  print("No")
  exit()
 else:
  pass
if re.sub(r"[a-z]","",t)=="":
  print("Yes")
else:
  print("No")