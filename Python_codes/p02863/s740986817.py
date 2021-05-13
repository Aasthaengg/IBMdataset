n,t = map(int,input().split())
dpa = [[0 for i in range(t)] for j in range(n+1)]
dpb = [[0 for i in range(t)] for j in range(n+1)]

for i in range(t):
   dpa[0][i] = 0
   dpb[0][i] = 0
abl = []
for _ in range(n):
   a,b = map(int,input().split())
   abl.append((a,b))

for i in range(n-1):
   for j in range(t):
      if j - abl[i][0] >= 0:
         dpa[i+1][j] = max(dpa[i][j], dpa[i][j-abl[i][0]] + abl[i][1])
      else:
         dpa[i + 1][j] = max(dpa[i][j], dpa[i + 1][j])

abl = abl[::-1]
for i in range(n-1):
   for j in range(t):
      if j - abl[i][0] >= 0:
         dpb[i+1][j] = max(dpb[i][j], dpb[i][j-abl[i][0]] + abl[i][1])
      else:
         dpb[i + 1][j] = max(dpb[i][j], dpb[i + 1][j])

abl = abl[::-1]
ans = 0
for i in range(t):
   for j in range(n):
      ans = max(ans, dpa[j][i]+dpb[n-j-1][t-i-1]+abl[j][1])

print(ans)