n,m = map(int,input().split())
L = [[] for i in range(n)]
ans = [0]*m
l = [list(map(int,input().split())) for i in range(m)]

for i in range(len(l)):
  L[l[i][0]-1].append([l[i][1],i+1])
  
for ind,lis in enumerate(L):
  lis.sort()
  for j in range(len(lis)):
    ans[lis[j][1] - 1] = str(ind+1).zfill(6) + str(j+1).zfill(6)
    
print(*ans,sep = '\n')