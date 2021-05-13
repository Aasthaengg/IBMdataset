s=str(input())
s=list(s)
s=list(set(s))
s.sort()
if len(s)>=3:
  if s[0]=="a" and s[1]=="b" and s[2]=="c":
    print("Yes")
  else:
    print("No")
else:
  print("No")