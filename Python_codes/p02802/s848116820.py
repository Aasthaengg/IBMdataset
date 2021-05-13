n,m=map(int,input().split())
d,c,wa=[0]*n,0,0
for _ in range(m):
    p,a=input().split()
    p=int(p)-1
    if d[p]!=-1:
        if 'W' in a:
            d[p]+=1
        else:
            wa+=d[p]
            d[p]=-1
            c+=1
print(c,wa)