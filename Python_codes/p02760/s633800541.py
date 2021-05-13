from sys import stdin
nii=lambda:map(int,stdin.readline().split())
lnii=lambda:list(map(int,stdin.readline().split()))

l=[lnii() for i in range(3)]

n=int(input())
for i in range(n):
  b=int(input())
  for h in range(3):
    for w in range(3):
      if l[h][w]==b:
        l[h][w]=-1

if l[0][0]==l[1][1]==l[2][2]==-1 or l[0][2]==l[1][1]==l[2][0]==-1:
  print('Yes')
  exit()
for i in range(3):
  if l[i].count(-1)==3:
    print('Yes')
    exit()
l2=list(zip(*l))
for i in range(3):
  if l2[i].count(-1)==3:
    print('Yes')
    exit()

print('No')