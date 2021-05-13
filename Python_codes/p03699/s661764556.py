n=int(input())
a=[]
for _ in range(n):
  s=int(input())
  a.append(s)
  
sum1=sum(a)
a=sorted(a)
ch=0
if sum1%10!=0:
  print(sum1)
else:
  for x in range(n):
    if a[x]%10!=0:
      print(sum1-a[x])
      ch+=1
      break
  if ch==0:
    print(0)