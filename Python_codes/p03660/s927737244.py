N=int(input())
E=[[] for i in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  a,b=a-1,b-1
  E[a].append(b)
  E[b].append(a)

F=[0]*N
S=[0]*N

stack=[]
# 番号、距離、親
stack.append([0,0,-1])
while stack:
  node=stack.pop()
  v=node[0]
  dist=node[1]
  parent=node[2]
  F[v]=dist
  childs=E[v]
  for child in childs:
    if child==parent:
      continue
    stack.append([child,dist+1,v])
  
stack=[]
# 番号、距離、親
stack.append([N-1,0,-1])
while stack:
  node=stack.pop()
  v=node[0]
  dist=node[1]
  parent=node[2]
  S[v]=dist
  childs=E[v]
  for child in childs:
    if child==parent:
      continue
    stack.append([child,dist+1,v])

FenWin=0
SunWin=0
for i in range(N):
  if F[i]<=S[i]:
    FenWin+=1
  else:
    SunWin+=1
print(("Snuke","Fennec")[FenWin>SunWin])