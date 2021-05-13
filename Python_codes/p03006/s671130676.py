import sys

N=int(input())
if N<=2:
  print(1)
  sys.exit(0)

xylist=[]
for i in range(N):
  x,y=map(int,input().split())
  xylist.append((x,y))
xylist.sort()
#print(xylist)

pqset=set()
for i in range(N):
  x1,y1=xylist[i]
  for j in range(i+1,N):
    x2,y2=xylist[j]
    p=x2-x1
    q=y2-y1
    pqset.add((p,q))
#print(len(pqset))
    
answer=50
for p,q in pqset:
  comp_num=N
  for i in range(N):
    x1,y1=xylist[i]
    for j in range(i+1,N):
      x2,y2=xylist[j]
      if p==x2-x1 and q==y2-y1:
        comp_num-=1
        
  answer=min(answer,comp_num)
    
print(answer)