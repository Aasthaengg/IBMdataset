t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

p,q=(a1-b1)*t1,(a2-b2)*t2
if p>0:
  p*=-1
  q*=-1
if p+q<0:
  print(0)
if p+q==0:
  print('infinity')
if p+q>0:
  s,t=divmod((-p),(p+q))
  print(s*2+1) if t!=0 else print(s*2)