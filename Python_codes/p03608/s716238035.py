#17:03
n,m,r = map(int,input().split())
must = list(map(lambda x: int(x)-1,input().split()))
inf = 10**18
wf = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
  wf[i][i] = 0
for _ in range(m):
  a,b,l = map(int,input().split())
  a -= 1
  b -= 1
  wf[a][b] = l
  wf[b][a] = l
for k in range(n):
  for i in range(n):
    for j in range(n):
      wf[i][j] = min(wf[i][j],wf[i][k]+wf[k][j])
#print(wf)
can = []
import itertools
for perm in itertools.permutations(range(r)):
  ans = 0
  for i in range(r-1):
    ans += wf[must[perm[i]]][must[perm[i+1]]]
  can.append(ans)
#print(can)
print(min(can))