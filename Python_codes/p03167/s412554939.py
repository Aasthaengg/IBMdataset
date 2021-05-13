a=input().split()
H=int(a[0])
W=int(a[1])
n_list=[[0 for i in range(W)] for i in range(H)]
m_list=[]
for i in range(H) :
  m_list.append(input())

for i in range(H) :
  if m_list[i][0]=='.' :
    n_list[i][0]=1
  else :
    break

for i in range(W) :
  if m_list[0][i]=='.' :
    n_list[0][i]=1
  else :
    break

for i in range(1,H) :
  for j in range(1,W) :
    if m_list[i][j]=='#' :
      n_list[i][j]=0
    else :
      n_list[i][j]=n_list[i-1][j]+n_list[i][j-1]
print(n_list[-1][-1]%(10**9+7))