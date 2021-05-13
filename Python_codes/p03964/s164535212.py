n=int(input())
tans=1
aans=1
for i in range(n):
  t,a = map(int,input().split())
  tt=(tans+t-1)//t
  at=(aans+a-1)//a
  mt=max([tt,at])
  tans=t*mt
  aans=a*mt
print(tans+aans)