n,m=map(int,input().split())
stu=[list(map(int, input().split())) for _ in range(n)]
che=[list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    a=stu[i][0]
    b=stu[i][1]
    minche=50
    minlen=10**10
    for j in range(m):
        x=che[j][0]
        y=che[j][1]
        kyori=abs(a-x)+abs(b-y)
        if kyori<minlen:
            minlen=kyori
            minche=j+1
    print(minche)