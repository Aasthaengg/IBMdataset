ans,result=0,0
for i in range(1,int(input())+1):
  count=0
  num=i
  while num%2==0:
    num//=2
    count+=1
  if ans < count:
    ans=count
    result=i
print(1 if not (ans and result) else result)