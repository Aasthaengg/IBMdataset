from itertools import groupby
n = int(input())
h = list(map(int,input().split()))
max_h = max(h)
for i in range(n):
    h[i] = [h[i],0]
ans = 0
for i in range(max_h):
    for is_more,group in groupby(h, key=lambda a:bool(a[0] > a[1])):
        group = list(group)
        if is_more:
            ans += 1
    for hs in h:
        hs[1] += 1
print(ans)