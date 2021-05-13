n=int(input())
a=[int(input()) for _ in range(n)]
from collections import Counter
ca=Counter(a)
ma=max(a)
if ca[ma]>1:
  ans=[ma]*n
  print(*ans,sep='\n')
else:
  ks=set(ca.keys())
  ks.discard(ma)
  maa=max(ks)
  for x in a:
    if x==ma:
      print(maa)
    else:
      print(ma)
