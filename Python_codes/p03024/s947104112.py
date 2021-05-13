s=input()
l=len(s)
count=0
for i in range(l):
  if(s[i]=='x'):
    count+=1
if(count>=8):
  print("NO")
else:
  print("YES")