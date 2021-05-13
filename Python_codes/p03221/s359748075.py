import sys
n,m = map(int, sys.stdin.readline().rstrip("\n").split())
city = {}
yton = {}
for i in range(m):
    p,y = map(int, sys.stdin.readline().rstrip("\n").split())
    if p not in city.keys():
        city[p] = []
        city[p].append(y)
        yton[y] = i
    else:
        city[p].append(y)
        yton[y] = i
ans = [None]*m
for p in city.keys():
    city[p].sort()
    for i,y in enumerate(city[p]):
        ans[yton[y]] = str(p*(10**6)+i+1).zfill(12)
print(*ans, sep = '\n') 