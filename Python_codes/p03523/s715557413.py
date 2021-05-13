s = input()
flag = 1

if s.find("AA") != -1:
  flag = 0
if s.find("KA") != -1:
  flag = 0
if s.find("IA") != -1:
  flag = 0

if s.replace("A","") != "KIHBR":
  flag = 0
  
if flag == 1:
  print("YES")
else:
  print("NO")
