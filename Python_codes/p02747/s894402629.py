s=input()
flag=True
for i in range(0,len(s),2):
  if "hi"==s[i:i+2]:
    continue
  else:
    flag=False
    break
if flag==True:
  print("Yes")
else:
  print("No")