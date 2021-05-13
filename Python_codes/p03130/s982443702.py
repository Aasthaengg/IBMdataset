from collections import defaultdict
d = defaultdict(list)
for i in range(3):
    a,b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

a = sorted([len(d[i]) for i in range(1,5)])
if a == [1,1,2,2]:
    print("YES")
else:print("NO")
# print(a)