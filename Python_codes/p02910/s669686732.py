s = str(input())
bool =False
for i in range (len(s)):
  if i % 2 == 0 and s[i] == 'L':
    bool = True
  elif i % 2 != 0 and s[i] == 'R':
    bool = True
if bool == True:
  print("No")
else:
  print("Yes")