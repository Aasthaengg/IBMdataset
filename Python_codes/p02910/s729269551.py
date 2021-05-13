S = input()
flag = True
for i in range(len(S)):
  if (i+1) % 2 == 1:
    if S[i] =="R" or S[i] =="U" or S[i] =="D":
      pass
    else:
      flag = False
      break
  else:
    if S[i] =="L" or S[i] =="U" or S[i] =="D":
      pass
    else:
      flag = False
      break
if flag:
  print("Yes")
else:
  print("No")