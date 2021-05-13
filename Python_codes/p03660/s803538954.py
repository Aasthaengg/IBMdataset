import itertools
import sys
input = sys.stdin.readline
def inputs():
    return [int(x) for x in input().split()]
N = int(input())
E = {i:[] for i in range(N+1)}
for i in range(N-1):
    a,b= inputs()
    E[a].append(b)
    E[b].append(a)
stkf = [[1,-1,0]]
visitedf=[0]*(N+1)
visiteds=[0]*(N+1)
stks = [[N,-1,0]]
cntf=0
cnts=0
while stkf:
    v,p,cost=stkf.pop()
    if v==N:
        visitedf[N]=cost
        continue
    visitedf[v]=cost
    cntf+=1
    for i in E[v]:
        if i!=p:
            stkf.append([i,v,cost+1])
while stks:
    v,p,cost=stks.pop()
    if v==1:
        visiteds[1]=cost
        continue
    visiteds[v]=cost
    cnts+=1
    for i in E[v]:
        if i!=p:
            stks.append([i,v,cost+1])
for i in range(1,N+1):
  if visitedf[i] and visiteds[i]:
    if visitedf[i]<=visiteds[i]:
      cnts-=1
    else:
      cntf-=1
#print(cntf-1,cnts-1,visitedf[N]-1,visiteds[1]-1)
"""
if (visitedf[N]-1)%2!=0:
  cntf=cntf-1-(visitedf[N]-1)//2
  cnts=cnts-1-(visitedf[N]-1)//2-1
else:
  cntf=cntf-1-(visitedf[N]-1)//2
  cnts=cnts-1-(visitedf[N]-1)//2
"""
print("Fennec" if cntf>cnts else "Snuke")
#print(visitedf,cntf,cnts)