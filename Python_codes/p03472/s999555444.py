import math
n,h = map(int,input().split())
l = []; x,y = 0,0
for _ in range(n):
    a,b = map(int,input().split())
    if a > x or a == x and b < y:
        x,y = a,b
    if b < x:continue
    l.append((a,b))
l.remove((x,y))
l = sorted(l,key=lambda x:-x[1])
ans = 0
for a,b in l:
    if b <= x:break
    if b < y and y >= h:
        print(ans+1);exit()
    h -= max(b,x)
    ans += 1
    if h <= 0:
        print(ans);exit()
d = math.ceil((max(0,h-y))/x)
print(ans + d + 1)
