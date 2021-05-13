def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

h,w = map(int,input().split()) 

d = [[float("inf")]*10 for i in range(10)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for i in range(10):
    l = list(map(int,input().split()))
    for j in range(10):
      d[i][j] = l[j]

a = [list(map(int,input().split())) for i in range(h)]
d1 = []
s = warshall_floyd(d)
for i in s:
  d1.append(i[1])
#print(d1)
su = 0
for i in a:
  for j in i:
    if j!=-1:
      su += d1[j]
print(su)