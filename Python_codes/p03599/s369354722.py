a,b,c,d,e,f=map(int,input().split())

wa=[]
su=[]
for i in range(1,31):
  for j in range(0,31):
    x=i-j*a
    if x>=0:
      if x%b==0:
        wa.append(i*100)
        
for p in range(1,3001):
  for q in range(0,3001):
    y=p-q*c
    if y>=0:
      if y%d==0:
        su.append(p)
        
wa1=list(set(wa))
su1=list(set(su))

ans=0
ans1=[]
for r in wa1:
  for t in su1:
    if r+t<=f and t/r <= e/100:
      if t/(r+t)>=ans:
        ans=t/(r+t)
        ans1.append([r,t])
        
if len(ans1)==0:
  print(str(wa[0])+' '+str(0))
else:
  W=ans1[-1][0]
  S=ans1[-1][1]
  print(str(W+S)+' '+str(S))