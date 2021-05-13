s=[i for i in input()]
s.sort()
if s[0]==s[1] and s[2]==s[3] and s[0]!=s[3]:
  print("Yes")
else:
  print("No")