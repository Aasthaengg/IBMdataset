import bisect
a,b,q = map(int,input().split())
s = [int(input()) for _ in range(a)]
t = [int(input()) for _ in range(b)]
for i in range(q):
    x = int(input())
    index1 = bisect.bisect(s,x)
    index2 = bisect.bisect(t,x)
    cands = []
    if index1 != 0:
        sl = x-s[index1-1]
    if index1 != a:
        sr = s[index1]-x
    if index2 != 0:
        tl = x-t[index2-1]
    if index2 != b:
        tr = t[index2]-x
    if index1 != 0:
        if index2 != 0:
            cands.append(max(sl,tl))
        if index2 != b:
            cands.append(sl*2+tr)
            cands.append(tr*2+sl)
    if index1 != a:
        if index2 != 0:
            cands.append(sr*2+tl)
            cands.append(sr+tl*2)
        if index2 != b:
            cands.append(max(sr,tr))
    print(min(cands))