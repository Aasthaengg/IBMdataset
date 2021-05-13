A,B,C = map (int,input().split())
list = [A,B,C]
list.sort()

if list[0] == list[1] == list[2]:
  if list[2]  < list[0] + list[1]:
    print("Yes")
  elif list[2]  == list[0] + list[1]:
    print("No")
  else:
    print("No")
     
else:
  print("No")