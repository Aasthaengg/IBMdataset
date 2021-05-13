def koch(p1,p2):
    s=[(2*p1[0]+p2[0])/3,(2*p1[1]+p2[1])/3]
    t=[(p1[0]+2*p2[0])/3,(p1[1]+2*p2[1])/3]
    m=[(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    mu=[-(p2[1]-p1[1])*3**.5/6,(p2[0]-p1[0])*3**.5/6]
    u=[m[0]+mu[0],m[1]+mu[1]]
    return [s,u,t]
ans=[[0,0],[100,0]]
n=int(input())
for _ in range(n):
    now=ans.copy()
    ans=[]
    l=0
    r=1
    c=len(now)
    while r<c:
        ans.append(now[l])
        ans+=koch(now[l],now[r])
        l+=1
        r+=1
    ans.append(now[l])
for p in ans:
    print(*p)
