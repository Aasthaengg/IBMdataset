h,w,a,b = map(int,input().split())

s = 1
t = 0

for i in range(h):
    res = []
    if s == 1 and i >= b:
        s,t = t,s
    for j in range(w):
        if j < a:
            res.append(s)
        else:
            res.append(t)
    else:
        print(*res, sep="")