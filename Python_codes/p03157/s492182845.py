belong=list()
group=list()
C=list()

def init(X):
  global belong,group,C
  belong=list(range(X))
  group=[[i] for i in range(X)]
  C=[[S[i//W][i%W]=='#',S[i//W][i%W]=='.'] for i in range(X)]

def unite(x,y):
  if len(group[belong[x]])<len(group[belong[y]]):
    x,y=y,x
  if belong[x]==belong[y]:
    return True
  z=belong[y]
  for i in range(len(group[z])):
    belong[group[z][-1]]=belong[x]
    group[belong[x]].append(group[z][-1])
    del group[z][-1]
  for i in range(2):
    C[belong[x]][i]+=C[z][i]
    C[z][i]=0
  return False

H,W=map(int,input().split())
S=[input() for i in range(H)]
init(H*W)
for i in range(H):
  for j in range(W):
    if i:
      if S[i][j]!=S[i-1][j]:
        unite(i*W+j,i*W+j-W)
    if j:
      if S[i][j]!=S[i][j-1]:
        unite(i*W+j,i*W+j-1)
    if i+1<H:
      if S[i][j]!=S[i+1][j]:
        unite(i*W+j,i*W+j+W)
    if j+1<W:
      if S[i][j]!=S[i][j+1]:
        unite(i*W+j,i*W+j+1)
P=0
for i in range(H*W):
  P+=C[i][0]*C[i][1]
print(P)