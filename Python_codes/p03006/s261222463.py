n=int(input())
pts=[list(map(int,input().split())) for _ in range(n)]

if n==1:
    print(1)
    exit(0)

ans=100

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return -1

for i in range(n):
    for j in range(i+1,n):
        x1,y1=pts[i]
        x2,y2=pts[j]

        p=x1-x2
        q=y1-y2

        visit=[0]*n
        
        cur=0
        for k in range(n):
            if visit[k]==1:
                continue
            cur+=1
            x3,y3=pts[k]
            cx=x3
            cy=y3
            while my_index(pts,[cx,cy])>=0:
                visit[my_index(pts,[cx,cy])]=1
                cx+=p
                cy+=q
            cx=x3
            cy=y3
            while my_index(pts,[cx,cy])>=0:
                visit[my_index(pts,[cx,cy])]=1
                cx-=p
                cy-=q
        
        ans=min(ans,cur)
    
print(ans)