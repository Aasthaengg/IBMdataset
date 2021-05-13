H,W,M = map(int,input().split())
hs = [0]*H
ws = [0]*W
s = set()
for i in range(M):
    h,w = map(int,input().split())
    hs[h-1] += 1
    ws[w-1] += 1
    s.add((h-1,w-1))

mh = 0; mw = 0
for i in range(H):
    mh = max(mh,hs[i])
for i in range(W):
    mw = max(mw,ws[i])

Is = []; Js = []
for i in range(H):
    if mh ==  hs[i]:
        Is.append(i)
for i in range(W):
    if mw == ws[i]:
        Js.append(i)
ans = mh + mw
flag = 0
for i in Is:
    for j in Js:
        if (i,j) in s:
            continue
        print(ans)
        exit()
print(ans-1)