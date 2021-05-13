n,m=map(int,input().split())
ss=[list(map(int,input().split())) for i in range(n)]
che=[list(map(int,input().split())) for i in range(m)]
for i in range(n):
    ans=100000000000000000000000000000000000000000000000000000
    x,y=ss[i]
    for  j in range(m):
        if ans>abs(x-che[j][0])+abs(y-che[j][1]):
            ans=abs(x-che[j][0])+abs(y-che[j][1])
            ind=j
    print(ind+1)
