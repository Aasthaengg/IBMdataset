#071_C
from collections import Counter
n = int(input())
a = list(map(int, input().split()))

c = Counter(a).most_common()
edges = []
for l, cnt in c:
    if cnt < 2:
        break
    else:
        edges.append(l)
        if cnt > 3:
            edges.append(l)
edges.sort(reverse= True)
if len(edges) < 2:
    print(0)
else:
    print(edges[0] * edges[1])