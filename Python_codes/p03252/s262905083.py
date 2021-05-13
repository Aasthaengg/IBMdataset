S=input()
T=input()
from collections import defaultdict
ds = defaultdict(str)
dt = defaultdict(str)
for s,t in zip(S,T):
  if ds[s]=='' or ds[s]==t:
    ds[s]=t
  else:
    print('No')
    exit(0)
  if dt[t]=='' or dt[t]==s:
    dt[t]=s
  else:
    print('No')
    exit(0)
print('Yes')