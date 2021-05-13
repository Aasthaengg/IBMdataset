def koch(p,q,n):
    if n==0:
        return [p]
    else:
        c1=[(p[0]*2+q[0])/3,(p[1]*2+q[1])/3]
        c3=[(p[0]+q[0]*2)/3,(p[1]+q[1]*2)/3]
        if p[0]<q[0]:
            if p[1]==q[1]:
                c2=[(p[0]+q[0])/2,p[1]+(q[0]-p[0])/2/3**0.5]
            elif p[1]<q[1]:
                c2=[p[0],(p[1]+q[1]*2)/3]
            else:
                c2=[q[0],(p[1]*2+q[1])/3]
        else:
            if p[1]==q[1]:
                c2=c2=[(p[0]+q[0])/2,p[1]+(q[0]-p[0])/2/3**0.5]
            elif p[1]<q[1]:
                c2=[q[0],(p[1]*2+q[1])/3]
            else:
                c2=[p[0],(p[1]+q[1]*2)/3]
        return koch(p,c1,n-1)+koch(c1,c2,n-1)+koch(c2,c3,n-1)+koch(c3,q,n-1)


n=int(input())
ans=koch([0,0],[100,0],n)+[[100,0]]
for i in ans:
    print(*i)
