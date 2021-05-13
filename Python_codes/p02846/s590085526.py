t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=a1-b1,a2-b2
if t1*c1+t2*c2==0:
  print('infinity')
else:
  # t1+t2でどれだけ二人が離れるか。
  d=t1*c1+t2*c2
  if c2*d<0:
    print(0)
  elif abs(t2*c2)<abs(d):
    print(0)
  else:
    tmp=((t2*c2)//d)
    if (t2*c2)%d==0:
      print(2*tmp-2)
    else:
      print(2*tmp-1)
