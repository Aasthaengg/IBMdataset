a,b=map(int,input().split())

A=[]
B=[]

for x in range(1,20001):
  if (x*8)//100==a:
    A.append(x)
  if (x*10)//100==b:
    B.append(x)
    
c=set(A)&set(B)

if len(c)==0:
  print(-1)
else:
  print(min(c))