from collections import defaultdict
n,m = map(int,input().split())
d = defaultdict(int)
for i in range(m):
    a,b = map(int,input().split())
    d[a] += 1
    d[b] += 1
ans = True
for i in d.values():
    if i % 2 != 0:
        ans = False
if ans:
    print("YES")
else:
    print("NO")