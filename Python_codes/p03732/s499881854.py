n,w=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
L=[[] for i in range(4)]
L2=[[0] for i in range(4)]
for i in range(n):
  L[l[i][0]-l[0][0]].append(l[i][1])
for i in range(4):
  L[i].sort()
  L[i].reverse()
for i in range(4):
  for j in range(len(L[i])):
    L2[i].append(L2[i][len(L2[i])-1]+L[i][j])
ansL=[]
for i1 in range(len(L2[0])):
  for i2 in range(len(L2[1])):
    for i3 in range(len(L2[2])):
      for i4 in range(len(L2[3])):
        if l[0][0]*i1+(l[0][0]+1)*i2+(l[0][0]+2)*i3+(l[0][0]+3)*i4<=w:
          ansL.append(L2[0][i1]+L2[1][i2]+L2[2][i3]+L2[3][i4])
print(max(ansL))