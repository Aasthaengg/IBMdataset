n,m=map(int,input().split())
a=[]
b=[]
for i in range(n):
    s=list(map(int,input().split()))
    a.append(s[0])
    b.append(s[1])
c=zip(a,b)
d=sorted(c)
#print(d)
#print(d[0][1])
yen=0
btl=0
for i in range(n):
    if d[i][1]+btl<m:
        yen+=d[i][0]*d[i][1]
        btl+=d[i][1]
    elif d[i][1]+btl>=m:
        yen+=d[i][0]*(m-btl)
        btl=m
    if btl==m:
        print(yen)
        exit()