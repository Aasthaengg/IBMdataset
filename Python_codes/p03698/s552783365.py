s=input()
for i in range(len(s)-1):
  for j in range(i+1,len(s)):
    if s[i]==s[j]:
      print("no")
      break
  else:
    continue
  break
else:
  print("yes")