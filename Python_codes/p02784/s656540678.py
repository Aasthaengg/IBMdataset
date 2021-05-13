a,b=map(int,input().split())
l=list(map(int,input().split()))
l[::-1]
s=0
f=0
for i in range(len(l)):
  s+=l[i]
  if s>=a:
    f=1
    break 
  else:
    continue
if f==1:
  print("Yes")
else:
  print("No")