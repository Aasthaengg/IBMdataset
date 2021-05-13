import math
n,h = map(int,input().split())
al = []
bl = []
ans = 0
for i in range(n):
    a,b = map(int,input().split())
    al += [a]
    bl += [b]
am = max(al)
bl.sort(reverse=1)
for i in bl:
    if i>am:
        ans += 1
        h -= i
        if h <= 0:
            break
    else:
        break
if h > 0:
    ans += math.ceil(h/am)
print(ans)