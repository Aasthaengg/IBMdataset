n,m=map(int, input().split())
abl=[list(map(int, input().split())) for _ in range(n)]
cd=[list(map(int, input().split())) for _ in range(m)]

for ab in abl:
    dis=10**18
    num=0
    for i in range(m):
        x2,y2=cd[i]
        if dis>abs(ab[0]-x2)+abs(ab[1]-y2):
            dis=abs(ab[0]-x2)+abs(ab[1]-y2)
            num=i
    print(num+1)
