s=input()
t=input()
if s in t[0:len(s)] and len(t) == len(s)+1:
  print("Yes")
else:
  print("No")