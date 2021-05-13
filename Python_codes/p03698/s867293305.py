s=input()
all_different=True
for i in range(len(s)-1):
  for j in range(i+1,len(s)):
    if s[i]==s[j]:
      all_different=False
  if not all_different:
     break
if all_different:
  print("yes")
else:
  print("no")