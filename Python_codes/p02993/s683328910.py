s=input()
c=0
for i in range(3):
  if s[i]==s[i+1]:
    c+=1
if c==0:
  print("Good")
else:
  print("Bad")