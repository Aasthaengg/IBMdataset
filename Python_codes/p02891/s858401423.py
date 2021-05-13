s=str(input())
k=int(input())
s=list(s)
s2=s+s
cnt=0
temp1=0
temp2=0
l=0
for i in range(1,len(s)):
  if s[i]==s[i-1]:
    cnt=cnt+1
    l=l+1
  if s[i]!=s[i-1]:
    temp1=temp1+(cnt+1)//2
    cnt=0
temp1=temp1+(cnt+1)//2
cnt=0
for i in range(1,len(s2)):
  if s2[i]==s2[i-1]:
    cnt=cnt+1
  if s2[i]!=s2[i-1]:
    temp2=temp2+(cnt+1)//2
    cnt=0
temp2=temp2+(cnt+1)//2
cnt=0
if l==len(s)-1:
  print(k*len(s)//2)
elif k==1:
  print(temp1)
else:
  print(temp1+(temp2-temp1)*(k-1))