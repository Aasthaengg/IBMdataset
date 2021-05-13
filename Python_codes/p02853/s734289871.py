x,y=map(int,input().split())
l=[1,2,3]
z=[300000,200000,100000]
if x==1 and y==1:
    print(1000000)
else:
    ans=0
    if x in [1,2,3]:
        ans+=z[l.index(x)]
    if y in [1,2,3]:
        ans+=z[l.index(y)]
    print(ans)