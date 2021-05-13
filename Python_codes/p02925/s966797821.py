from collections import defaultdict
N = int(input())
dic = defaultdict(list)
toNum = {}
L = N*(N-1)//2
s = [0]
for i in range(N-1,0,-1):
  s += [s[-1]+i]
dist = [0]*L
for i in range(N):
  inf = [int(c)-1 for c in input().split()]
  pa = min(i,inf[0])
  pb = max(i,inf[0])
  pnum = s[pa]+(pb-pa-1)
  for j in range(1,N-1):
    a = min(i,inf[j])
    b = max(i,inf[j])
    num = s[a]+(b-a-1)
    dic[pnum]  += [num]
    dist[num] += 1
    pa = a
    pb = b
    pnum = num

hq = []
ans = 0
for i in range(L):
  if dist[i]==0:
    hq += [i]
while hq:
  ans += 1
  nq = []
  for e in hq:
    for p in dic[e]:
      if dist[p]==0:
        continue
      dist[p] -= 1
      if dist[p]==0:
        nq += [p]
  hq = nq
if sum(dist) != 0:
  ans = -1
print(ans)