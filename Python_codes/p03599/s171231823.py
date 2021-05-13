a,b,c,d,e,f=map(int,input().split())
ans=[]
for aa in range(31):
  for bb in range(31):
    w=100*(aa*a+bb*b)
    if w>f:break
    n=min(f-w,e*(aa*a+bb*b))
    for cc in range(3001):
      s=cc*c
      if s>n:break
      nn=n-s
      ss=d*(nn//d)
      su=s+ss
      wa=w
      if wa+su==0:continue
      ans.append([100*su/(wa+su),wa,su])
ans.sort(reverse=1)
_,w,s=ans[0]
print(w+s,s)