n=int(input())
l=[0]*87
l[0]+=2
l[1]+=1
if n==1:
  print(1)
else:
  for i in range(2,n+1):
    l[i]=l[i-1]+l[i-2]
  print(l[n])