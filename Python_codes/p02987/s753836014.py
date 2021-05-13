a=list(input())
b=set(a)
count=0
for i in range(4):
  if a[0]==a[i]:
    count+=1
if len(b)==2 and (count==2):
  print('Yes')
else:
  print('No')
