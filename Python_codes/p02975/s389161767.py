n=int(input())
a=list(map(int,input().split()))

if a.count(0)==n:
  print('Yes')
  exit()

if n%3!=0:
  print('No')
  exit()


x=list(set(a))

z=[]

if len(x)>3:
  print('No')
  exit()

for i in x:
  if a.count(i)==n//3:
    z+=[i]
  
  elif a.count(i)==(n//3)*2:
    z+=[i]
    z+=[i]

  elif a.count(i)==n:
    z+=[i]
    z+=[i]
    z+=[i]

  else:
    print('No')
    exit()


ans=0

for i in z:
  ans^=i

if ans==0:
  print('Yes')

else:
  print('No')
