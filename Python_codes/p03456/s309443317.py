d=[]
i=1
while i*i<100101:
  d.append(i*i)
  i+=1
a,b=input().split()
if int(a+b) in d:
  print("Yes")
else:
  print("No")