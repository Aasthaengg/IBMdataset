from collections import deque
N=int(input())
point=[list(map(int,input().split())) for _ in range(N)]
ans=float("inf")
for i in range(N):
    for j in range(i+1,N):
        x1,y1=point[i]
        x2,y2=point[j]
        vec=[x1-x2,y1-y2]
        tree=[[] for _ in range(N)]
        col=[-1]*N
        for k in range(N):
            for l in range(k+1,N):
                xa, ya = point[k]
                xb, yb = point[l]
                if ((vec[0]==xa-xb)and(vec[1]==ya-yb))or((-vec[0]==xa-xb)and(-vec[1]==ya-yb)):
                    tree[k-1].append(l-1)
                    tree[l-1].append(k-1)
        for k in range(N):
            d=deque()
            if col[k]==-1:
                d.append(k)
            while len(d)>0:
                v=d.popleft()
                col[v]=k
                for l in tree[v]:
                    if col[l]==-1:
                        d.append(l)
        #print(col)
        #print(set(col))
        ans=min(ans,len(set(col)))
if N==1:
    print(1)
else:
    print(ans)