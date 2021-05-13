n=int(input())
count=1
index=1
while count<n:
  index+=1
  count+=index
if count!=n:
  print("No")
elif n==1:
  print("Yes")
  print(2)
  print("1 1")
  print("1 1")
else:
  print("Yes")
  print(index+1)
  l=[]
  now=1
  num=1
  while now<n:
    l.append(now)
    now+=num
    num+=1
  for i in range(index):
    l1=[str(index)]
    l1.append(str(l[i]))
    num=l[i]
    count1=0
    while count1<i:
      num+=1
      count1+=1
      l1.append(str(num))
    for j in range(1+i,index):
      num+=j
      l1.append(str(num))
    print(" ".join(l1))
  l1=[str(index),str(l[0])]
  num=0
  for j in range(2,index+1):
    num+=j
    l1.append(str(l[0]+num))
  print(" ".join(l1))
