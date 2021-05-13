from bisect import bisect_left as bt
n,m = map(int,input().split())
dm,ct = [[] for _ in range(n+1)],[]
for _ in range(m):
  a,b = map(int,input().split())
  dm[a].append(b); ct.append((a,b))
for i in range(1,n+1):
  dm[i].sort()
for c in ct:
  v,f = str(c[0]),str(bt(dm[c[0]],c[1])+1)
  print('0'*(6-len(v))+v+'0'*(6-len(f))+f)