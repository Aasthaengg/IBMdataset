from collections import Counter

G=[[] for _ in range(4)]

for i in range(3):
  a,b=map(int,input().split())
  G[a-1].append(b-1)
  G[b-1].append(a-1)
  
deg = [len(G[i]) for i in range(4)]

c = Counter(deg)

cnt=0
for k in c.keys():
  if k%2: cnt += c[k]
    
if cnt in (0,2):
  print('YES')
else:
  print('NO')