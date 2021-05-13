n = int(input())
mi = []
pl = []

l = list(map(int,input().split()))
for i in l:
    if i >= 0:
        pl.append(i)
    else:
        mi.append(i)
pl.sort()
mi.sort()
if n == 2:
    print(max(l)-min(l))
    print(max(l),min(l))
    exit()

if pl and mi:
    ans = []
    np = pl[-1]
    for i in range(1,len(mi)):
        ans.append([np,mi[i]])
        np -= mi[i]
    nm = mi[0]
    for i in range(len(pl)-1):
        ans.append([nm,pl[i]])
        nm -= pl[i]
    ans.append([np,nm])
    print(np-nm)
    for i in ans:
        print(*i)
elif pl:
    ans = []
    ans.append([pl[0],pl[1]])
    nm = pl[0]-pl[1]
    for i in range(2,len(pl)-1):
        ans.append([nm,pl[i]])
        nm -= pl[i]
    ans.append([pl[-1],nm])
    print(pl[-1]-nm)
    for i in ans:
        print(*i)
else:
    ans = []
    ans.append([mi[-1],mi[-2]])
    np = mi[-1]-mi[-2]
    for i in range(1,len(mi)-2):
        ans.append([np,mi[i]])
        np -= mi[i]
    ans.append([np,mi[0]])
    print(np-mi[0])
    for i in ans:
        print(*i)
