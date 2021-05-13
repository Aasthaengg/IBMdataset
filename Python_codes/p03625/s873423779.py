from collections import Counter as C
n,*a=map(int,open(0).read().split())
b=[]
for i in C(a).items():
  if i[1]>3:
    b+=[i[0],i[0]]
  elif i[1]>1:
    b+=[i[0]]
b=sorted(b)
print(b[-1]*b[-2] if len(b)>1 else 0)