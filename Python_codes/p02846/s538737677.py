T1,T2=map(int,input().split())
A1,A2=map(int,input().split())
B1,B2=map(int,input().split())

if B1>A1:
  A1,A2,B1,B2=B1,B2,A1,A2
  
if A1*T1+A2*T2>B1*T1+B2*T2:
  print(0)
  exit()
if A1*T1+A2*T2==B1*T1+B2*T2:
  print("infinity")
  exit()

x=(T1*A1-T1*B1)//((B1-A1)*T1+(B2-A2)*T2)+1
ans=2*x-1
if (T1*A1-T1*B1)%((B1-A1)*T1+(B2-A2)*T2)==0:
  ans-=1
print(ans)