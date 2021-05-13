import sys
def input():
    return sys.stdin.readline()[:-1]
H,W,M=map(int,input().split())
s={tuple(map(lambda x: int(x)-1, input().split())) for i in range(M)}
lh=[0]*H
lw=[0]*W
for i in s:
    lh[i[0]]+=1
    lw[i[1]]+=1
mh=max(lh)
mw=max(lw)
sh=[]
sw=[]
for i in range(H):
    if lh[i]==mh:
        sh.append(i)
for i in range(W):
    if lw[i]==mw:
        sw.append(i)
if len(sh)*len(sw)>M:
    print(mh+mw)
else:
    for i in sh:
        for j in sw:
            if (i,j) not in s:
                print(mh+mw)
                break
        else:
            continue
        break
    else:
        print(mh+mw-1)