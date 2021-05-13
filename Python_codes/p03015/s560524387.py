b=input()
m=10**9+7

t1,t2=1,2
for c in list(b)[1:]:
  t1*=3
  if c=='1':
    t1+=t2
    t2=(t2*2)%m
  t1%=m

print((t1+t2)%m)
