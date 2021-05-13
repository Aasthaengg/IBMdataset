s = input()
flag = False
for i in range(len(s)):
  if s[i]=='C':
    for j in range(i+1,len(s)):
      if s[j] == 'F':
        flag = True
        break
    if flag:
      break
if flag:
  print("Yes")
else:
  print("No")
