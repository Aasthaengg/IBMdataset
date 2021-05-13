def warshall_floyd(d):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

h,w=map(int,input().split())
DP=[list(map(int,input().split())) for i in range(10)]

table=warshall_floyd(DP)

cnt=[]
ans=0

for i in range(h):
  cnt+=list(map(int,input().split()))


for i in cnt:
  if i==-1:
    continue
  ans+=table[i][1]


print(ans)