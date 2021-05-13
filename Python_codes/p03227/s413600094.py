s=input()
if len(s)==2:
  print(s)
else:
  s=list(reversed(s))
  print(*s,sep="")