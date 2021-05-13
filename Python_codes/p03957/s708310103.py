s=str(input())
s=list(s)
temp=0
for i in range(len(s)):
  if s[i]=="C":
    temp=1
  if temp==1 and s[i]=="F":
    temp=2
if temp==2:
  print("Yes")
else:
  print("No")
