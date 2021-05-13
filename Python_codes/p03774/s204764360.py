n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
cd=[list(map(int,input().split())) for i in range(m)]

for a,b in ab:
    ans=-1
    kyori=float('inf')
    i=1
    for c,d in cd:
        if kyori>abs(a-c)+abs(b-d):
            ans=i
            kyori=abs(a-c)+abs(b-d)
        i+=1
    print(ans)