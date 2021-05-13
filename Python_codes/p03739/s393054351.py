n=int(input())
a=list(map(int,input().split()))
tmp=0
csum_a=[]
for ai in a:
  tmp+=ai
  csum_a.append(tmp)
ans=0
tmp=0
plus=True
for si in csum_a:
  if plus and si+tmp>0:
    pass
  elif plus and si+tmp<=0:
    ans+=1-(si+tmp)
    tmp+=1-(si+tmp)
  elif not plus and si+tmp<0:
    pass
  elif not plus and si+tmp>=0:
    ans+=1+(si+tmp)
    tmp-=1+si+tmp
  plus=not plus

ans0=ans
ans=0
tmp=0
plus=False
for si in csum_a:
  if plus and si+tmp>0:
    pass
  elif plus and si+tmp<=0:
    ans+=1-(si+tmp)
    tmp+=1-(si+tmp)
  elif not plus and si+tmp<0:
    pass
  elif not plus and si+tmp>=0:
    ans+=1+(si+tmp)
    tmp-=1+si+tmp
  plus=not plus

print(min(ans0,ans))