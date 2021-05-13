N,A,B,C,D=map(int,input().split())
str=input()

str_ac = str[A-1:C]
str_bd = str[B-1:D]
str_bd2 = str[B-2:D+1]
#print(str_bd)
#print(str_ac)
#print(str_bd2)

if C<D:
  if str_bd.find("##")!=-1 or str_ac.find("##")!=-1:
    print("No")
  else:
    print("Yes")
else:
  if str_bd.find("##")!=-1 or str_ac.find("##")!=-1:
    print("No")
  else:
    if str_bd2.find("...")!=-1:
      print("Yes")
    else:
      print("No")