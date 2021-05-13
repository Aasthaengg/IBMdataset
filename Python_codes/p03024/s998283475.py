count=0
s=input()
for i in range(0,len(s)):
  if(s[i]=='x'):
    count=count+1
if(count>=8):
  print("NO")
else:
  print("YES")