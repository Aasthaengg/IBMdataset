d,n=map(int,input().split())

if d==0:
  cnt=0
  i=1
  while 1:
    if i%100!=0:
      cnt+=1
    if cnt==n:
      print(i)
      exit()
    i+=1
else:
  cnt=0
  i=1
  waru=100**d
  while 1:
    if i%waru==0 and (i//waru)%100 !=0 :
      cnt+=1
    if cnt==n:
      print(i)
      exit()
    i+=1
