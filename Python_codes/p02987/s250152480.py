s=input()
if s.count(s[0])==2:
  if s[1]==s[2] or s[1]==s[3] or s[2]==s[3]:
    print("Yes")
  else:
    print("No")
else:
  print("No")