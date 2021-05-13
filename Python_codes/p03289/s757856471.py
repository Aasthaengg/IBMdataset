s=input()
ls=len(s)
c1=s[0]=="A"
c2=list(s[2:ls-1]).count("C")==1
if c1 and c2:
  s=s.replace("A", "a")
  s=s.replace("C", "c")
  if s.islower():
    print("AC")
  else:
    print("WA")
else:
  print("WA")