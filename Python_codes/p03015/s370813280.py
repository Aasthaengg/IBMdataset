n=int(input())
num=len(str(n))-1
l=[]
ans=1
mod=10**9+7
for i in range(num):
  ans=(ans*3)%mod
  l.append(ans)
w=str(n)
now=2
for i in range(1,num):
  if w[i]=="0":
    pass
  else:
    ans=(ans+now*l[-i-1])%mod
    now=(now*2)%mod
if w[-1]=="0":
  ans=(ans+now)%mod
else:
  ans=(ans+3*now)%mod
if n==1:
  print(3)
else:
  print(ans)