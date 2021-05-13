l=list(input())
if l[0]==l[1]==l[2]==l[3]:
  print("No")
elif l[0]==l[1] and l[2]==l[3]:
  print("Yes")
elif l[0]==l[2] and l[1]==l[3]:
  print("Yes")
elif l[0]==l[3] and l[1]==l[2]:
  print("Yes")
else:
  print("No")