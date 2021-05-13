N,K=map(int,input().split())
E=[[] for i in range(N)]
for i in range(N-1):
  a,b=map(int,input().split())
  E[a-1].append(b-1)
  E[b-1].append(a-1)

DIV=10**9+7
ans=1
stack=[]
# 番号、選べる色、親フラグ（初回だけ全色選べる）
stack.append([0,K,-1])
while stack:
  node=stack.pop()
  v=node[0]
  color=node[1]
  parent=node[2]
  ans=((ans%DIV)*color)%DIV
  nextcolor=K-2
  if parent==-1:
    nextcolor=K-1
  children=E[v]
  for child in children:
    if child==parent:
      continue
    if nextcolor==0:
      ans=0
      break
    stack.append([child,nextcolor,v])
    nextcolor-=1
else:
  print(ans)
