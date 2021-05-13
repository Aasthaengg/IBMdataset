from collections import defaultdict

n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
if n == 1:
    print(1)
    exit()
d = defaultdict(int)
for i in range(n):
    for j in range(n):
        if i== j:
            continue
        a,b = l[i]
        c,e = l[j]
        d[(a-c,b-e)] += 1
ans = n
m = max(d.values())
for i,j in d.items():
    if j != m:
        continue

    x,y = i
    if x==0 and y == 0:
        continue
    count = 0
    for c,d in l:
        if [c+x,d+y] in l:
            count += 1
    ans = min(ans,n-count)
print(ans)