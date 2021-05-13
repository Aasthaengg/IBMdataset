n=int(input())
xy=[tuple(map(int,input().split())) for _ in range(n)]
pq=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        sx,sy=xy[i]
        gx,gy=xy[j]
        pq.append((gx-sx,gy-sy))



ans=n
for p,q in pq:
    now=0
    for x,y in xy:
        if (x+p,y+q) not in xy:
            now+=1
    ans=min(ans,now)

print(ans)
