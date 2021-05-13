from collections import Counter
import heapq

n = int(input())
v = list(map(int, input().split()))
o = [x for x in v[0:n:2]]
e = [x for x in v[1::2]]
oc = Counter(o)
ec = Counter(e)
ocfreq = [(x[1]*(-1),x[0]) for x in oc.items()]
ecfreq = [(x[1]*(-1),x[0]) for x in ec.items()]
heapq.heapify(ocfreq)
heapq.heapify(ecfreq)
o1 = heapq.heappop(ocfreq)
e1 = heapq.heappop(ecfreq)
if o1[1] != e1[1]:
    print(n+o1[0]+e1[0])
else:
    if len(ocfreq) == 0 and len(ecfreq) == 0:
        print(n//2)
    elif len(ocfreq) == 0:
        e2 = heapq.heappop(ecfreq)
        print((n//2)+e2[0])
    elif len(ecfreq) == 0:
        o2 = heapq.heappop(ocfreq)
        print((n//2)+o2[0])
    else:
        e2 = heapq.heappop(ecfreq)
        o2 = heapq.heappop(ocfreq)
        print(n+min(o1[0]+e2[0],o2[0]+e1[0]))