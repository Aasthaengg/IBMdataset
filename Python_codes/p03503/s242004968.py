n=int(input()) #　a1
f = [list(map(int, input().split())) for i in range(n)]
p=[list(map(int, input().split())) for i in range(n)]

numf=[]
ansp=0
ans=-float('inf')

for i in range(1,2**10):
  l=str(bin(i)).lstrip("0b")
  ll=list(l.zfill(10))
  ilist=[int(xl) for xl in ll]
  j=0
  ansp=0
  for jlist in f:
    suml=[ilist[k]*jlist[k] for k in range(10)]
    c=sum(suml)
    ansp+=p[j][c]
    j+=1

  ans=max(ans,ansp)

print(ans)