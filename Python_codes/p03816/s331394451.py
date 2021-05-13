N=int(input())
A=sorted([int(c) for c in input().split()])
D={c:0 for c in A}
for a in A:
  D[a]+=1
tmp=0
for d in D:
  D[d]=(D[d]+1)%2+1
  if(D[d]==2):
    tmp+=1
if(tmp%2==1):
  print(len(D)-1)
else:
  print(len(D))