H,W,N=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N)]

from collections import defaultdict
from collections import Counter

ANS = defaultdict(int)

for a,b in AB:
    for i in [a-1,a,a+1]:
        for j in [b-1,b,b+1]:
            if 2<=i<H and 2<=j<W:
                ANS[(i,j)]+=1

counter=Counter(ANS.values())
ANSLIST=[0]*10
for c in counter:
    ANSLIST[c]=counter[c]
ANSLIST[0]=(H-2)*(W-2)-sum(counter.values())

for a in ANSLIST:
    print(a)