read=lambda :list(map(int,input().split()))
n=int(input())
t,a=read(),read()
mod=10**9+7
t=[(i!=j,i) for i,j in zip(t,[0]+t)]
a=[(i!=j,i) for i,j in zip(a,(a+[0])[1:])]

ans=1
for p,q in zip(t,a):
  if(p[0]):
    if(q[0]):
      if(p[1]!=q[1]):
        print(0)
        exit()  
    elif(q[1]<p[1]):
      print(0)
      exit()
  elif(q[0]):
    if(p[1]<q[1]):
      print(0)
      exit()
  else:
	  ans=ans*min(p[1],q[1])%mod
print(ans) 
