n=int(input())
ar=[int(i) for i in input().strip().split(" ")]
from collections import defaultdict
ev=defaultdict(int)
od=defaultdict(int)

def g(i):
    return (i[1],i[0])

for i in range(0,n,2):
    od[ar[i]]+=1

for i in range(1,n,2):
    ev[ar[i]]+=1

odd=list(od.items())
even=list(ev.items())
odd.append((0,0))
even.append((0,0))
odd.sort(key=g)
even.sort(key=g)

o1=odd[-1]
o2=odd[-2]
e1=even[-1]
e2=even[-2]
if o1[0]!=e1[0]:
    print(n-o1[1]-e1[1])
else:
    a1=(n-o1[1]-e2[1])
    a2=(n-o2[1]-e1[1])
    print(min(a1,a2))

