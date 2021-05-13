H,W,M=map(int,input().split())
bombh=[]
bombw=[]
bomb=[]
w=[0]*W
h=[0]*H
for i in range(M):
    hs,ws=map(int,input().split())
    w[ws-1]+=1
    h[hs-1]+=1
    bomb.append([hs-1,ws-1])
maxh=max(h)
maxw=max(w)
ans=maxh+maxw
count=0
for i in range(M):
    if ans==h[bomb[i][0]]+w[bomb[i][1]]:
        count+=1
a=h.count(maxh)*w.count(maxw)
if a==count:
    ans-=1
print(ans)