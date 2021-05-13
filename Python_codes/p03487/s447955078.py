from collections import Counter
N=int(input())
a=list(map(int,input().split()))

c = Counter(a)
ans=0
for k in c.keys():
  val = c[k]
  if val>k:ans+=val-k
  elif val<k:ans+=val
print(ans)