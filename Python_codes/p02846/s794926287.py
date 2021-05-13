t1, t2=map(int, input().split())
a1, a2=map(int, input().split())
b1, b2=map(int, input().split())

if (a1-b1)*(a2-b2)>0:
  print(0)
elif a1*t1+a2*t2==b1*t1+b2*t2:
  print('infinity')
else:
  if a1>b1:
    da=(a1-b1)*t1
    db=(b2-a2)*t2
    
    if da>db:
      print(0)
    else:
      temp=da//(db-da)
      if da%(db-da)>0:
        temp=2*temp
      else:
        temp=2*temp-1
      print(temp+1)
  else:
    db=(b1-a1)*t1
    da=(a2-b2)*t2
    
    if db>da:
      print(0)
    else:
      temp=db//(da-db)
      if db%(da-db)>0:
        temp=2*temp
      else:
        temp=2*temp-1
      print(temp+1)