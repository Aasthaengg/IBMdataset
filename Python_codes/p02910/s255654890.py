s = input()

s = list(s)
answer = True
for i in range(len(s)):
  if i%2 == 0:
    if(s[i] == "L"):
      answer = False
      break
  else:
    if(s[i] == "R"):
      answer = False

if answer :
  print("Yes")
else :
  print("No")