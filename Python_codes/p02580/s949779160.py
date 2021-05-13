import sys
from collections import defaultdict,Counter
input = sys.stdin.readline
h,w,m=map(int, input().split())
hs=[]
ws=[]
hw=defaultdict(int)
for i in range(m):
    h0,w0=map(int, input().split())
    hw[(h0,w0)]+=1
    hs.append(h0)
    ws.append(w0)

hd=Counter(hs)
wd=Counter(ws)
hmax=max(hd.values())
wmax=max(wd.values())

max_h_list=[kv[0] for kv in hd.items() if kv[1] == hmax]
max_w_list=[kv[0] for kv in wd.items() if kv[1] == wmax]
ans=float('inf')

for x in max_h_list:
    for y in max_w_list:
        if hw[(x,y)]==1:
            ans=min(ans,1)
        else:
            ans=min(ans,0)
            break
print(hmax+wmax-ans)