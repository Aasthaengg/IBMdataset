n=int(input())
a=list(map(int,input().split()))
b=sum(a)
c=1
ans=1
if a[0]==1 and n==0:
    print(1)
    exit()
if a[0]>0:
    print(-1)
    exit()
for i in a[1:]:
    b-=i
    c=min(c*2-i,b)
    ans+=c
    if c<0:
        print(-1)
        exit()
print(ans+sum(a))