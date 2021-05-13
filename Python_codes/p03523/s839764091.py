s=input()
t="AKIHABARA"
pos=0
for i in range(len(t)):
  while pos<len(s):
    if t[i]==s[pos]:
      pos+=1
      break
    else:
      break
if pos!=len(s):
  print('NO')
else:
  if "K" in s and "I" in s and "H" in s and "B" in s and "R" in s:
    print('YES')
  else:
    print('NO')