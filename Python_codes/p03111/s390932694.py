n,a,b,c = map(int,input().split())
m = [a,b,c]
l = sorted([int(input()) for i in range(n)])

import itertools 
data = list(itertools.product(range(4), repeat = n))

ans = float('inf')
for d in data:
    x = [[] for i in range(4)]
    for i in range(n):
        x[d[i]].append(l[i])
    if len(x[0])<1 or len(x[1])<1 or len(x[2])<1:
        continue
    buf = 0
    for i in range(3):
        buf += 10*(len(x[i])-1)
        buf += abs(sum(x[i])-m[i])

    ans = min(ans,buf)
print(ans)

