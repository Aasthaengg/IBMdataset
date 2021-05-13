w,a,b=map(int,input().split())
aa=a+w
bb=b+w
if b>=a:
  d=b-aa
  if d<=0:
    print(0)
  else:
    print(d)
else:
  d=a-bb
  if d<=0:
    print(0)
  else:
    print(d)