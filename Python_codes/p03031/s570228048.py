import itertools

n,m=map(int,input().split())

lis=[]

for _ in range(m):
  lis.append(list(map(int,input().split())))

p=list(map(int,input().split()))

ans=0
for binary in itertools.product([0,1],repeat=n):
  check=0
  for i in range(m):
    numon=0
    ki=lis[i][0]
    for j in range(ki):
      numon+=binary[lis[i][j+1]-1]
    if (numon+p[i])%2!=0:
      check+=1
  if check==0:
    ans+=1

print(ans)