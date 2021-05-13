from collections import defaultdict
n,k=map(int,input().split())
dd=defaultdict(lambda: 0)
for i in range(n):
  a,b=map(int,input().split())
  dd[a]+=b
cur_k=k
for k in sorted(dd.keys()):
  v=dd[k]
  cur_k-=v
  if cur_k <= 0:
    print(k)
    exit()
