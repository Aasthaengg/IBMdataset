n,m=map(int,input().split())
li=[list(map(int,input().split())) for i in range(m)]
li=sum(li,[])

for j in range(n):
    print(li.count(j+1))