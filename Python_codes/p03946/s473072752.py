n,t=map(int,input().split())
l=list(map(int,input().split()))
mi=l[0]
ri=0
t=0
ans=0
for i in l[1:]:
    mi=min(mi,i)
    ma=i 
    if ri<ma-mi:
        ri=ma-mi
        ans=1
    elif ri==ma-mi:
        if t:
            ans+=1
            t=0
    else:
        t=1
print(ans)