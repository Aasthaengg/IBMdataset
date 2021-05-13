n = int(input())
dat = list(map(int, input().split()))
f = True
res = []
while len(dat) > 0:
    t = -1
    for i in range(len(dat)):
        if i+1 == dat[i]:
            t = i
    if t == -1:
        f = False
        break
    res.append(dat[t])
    del dat[t]
if f is False:
    print(-1)
else:
    res.reverse()
    print("\n".join(list(map(str, res))))