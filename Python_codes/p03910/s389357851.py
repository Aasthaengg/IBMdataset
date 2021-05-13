n=int(input())

ans=[]
num=0

i=1
while num<n:
  num+=i
  ans.append(i)
  i+=1
else:
  sa=num-n

if sa!=0:
  ans.remove(sa)

for i in ans:
  print(i)