n,m=map(int,input().split())
stu=[list(map(int,input().split())) for _ in range(n)]
cp=[list(map(int,input().split())) for _ in range(m)]
for x1,y1 in stu:
    dist=10**18
    num=0
    for i in range(m):
        x2,y2=cp[i]
        if dist>abs(x1-x2)+abs(y1-y2):
            dist=abs(x1-x2)+abs(y1-y2)
            num=i
    print(num+1)