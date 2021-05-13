A,B,T=map(int,input().split())


count=0
i=1
t=A
while t<T+0.5:
  count=count+B
#  print(i,t,count)
  i=i+1
  t=i*A  

print(count)
