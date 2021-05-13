abc=list(map(int, input().split()))
k=int(input())
a=abc[0]
b=abc[1]
c=abc[2]

num=0
if(a < b):
  if(b < c):
    print("Yes")
  else:
    while num<k:
      c=2*c
      num=num+1
      if(b<c):
        print("Yes")
        break
    if(b>=c):
      print("No")
else:
  while num<k:
    b=2*b
    num=num+1
    if(a<b):
      break
  if(a<b):
    while num<k:
      c=2*c
      num=num+1
      if(b<c):
        print("Yes")
        break
    if(b>=c):
      print("No")
  else:
    print("No")