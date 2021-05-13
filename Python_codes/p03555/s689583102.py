s= input()
t= input()
flag = True
for i in range(3):
  if s[i] != t[2-i]:
    flag =False
if flag:
  print("YES")
else:
  print("NO")