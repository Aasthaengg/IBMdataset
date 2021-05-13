from collections import Counter
n,*v = map(int,open(0).read().split())
v1 = Counter(v[::2])
v2 = Counter(v[1::2])
v1 = sorted([(i,v1[i]) for i in v1.keys()],key =lambda x:x[1],reverse=True)
v2 = sorted([(i,v2[i]) for i in v2.keys()],key =lambda x:x[1],reverse=True)
if v1[0][0] != v2[0][0]:
  print(n-v1[0][1]-v2[0][1])
else:
  e1 = n-v2[0][1] if len(v1) == 1 else n-v1[1][1]-v2[0][1]
  e2 = n-v1[0][1] if len(v2) == 1 else n-v1[0][1]-v2[1][1]
  print(min(e1,e2))