import bisect
a,b,c,d,e,f = map(int,input().split())
lw = []
ls = []
for i in range((f//100)//b+1):
    for j in range(100):
        if b*i*100+a*j*100 > f:
            break
        lw.append(b*i*100+a*j*100)
for i in range((f//2)//d+1):
    for j in range(3000):
        if (d*i+c*j) > (f*e)/(100+e):
            break
        ls.append(d*i+c*j)
ls.sort()
lw.sort()
n = len(lw)
ans = 0
ansl = [0,0]

for i in range(n):
    w = lw[i]
    t = min(f-w,w/100*e)
    s = ls[bisect.bisect_right(ls,t)-1]
    if (s+w)==0:
        continue
    if 100*s/(s+w) >= ans:
        ans = 100*s/(s+w)
        ansl = [s+w,s]
print(*ansl)