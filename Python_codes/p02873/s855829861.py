import itertools
S=input()
N=len(S)+1
ans=0
KEY=[]
gr=itertools.groupby(list(S))
i=0
for key,group in gr:
  n=len(list(group))
  ans+=n*(n+1)//2
  KEY+=[n]
  if key==">" and i!=0:
    ans-=min(KEY[i-1],KEY[i])
  i+=1
print(ans) 