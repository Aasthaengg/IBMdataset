n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
l=sorted(l)
drink=0
money=0
index=0
while(drink<m):
    if l[index][1]+drink<m:
        drink+=l[index][1]
        money+=l[index][0]*l[index][1]
        index+=1
    else:
        money+=l[index][0]*(m-drink)
        drink=m
        print(money)
        break