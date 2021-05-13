s=str(input())
l=[s[0],s[1],s[2],s[3]]
l.sort()
if l[0]==l[1] and l[2]==l[3] and l[0]!=l[2]:
  print("Yes")
else:
  print("No")