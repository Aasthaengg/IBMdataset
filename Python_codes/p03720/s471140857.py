n,m=map(int,input().split())
result=[]
for _ in range(m):
    a,b=map(int,input().split())
    result.append(a)
    result.append(b)
count=0
for x in range(1,n+1):
    for i in result:
        if x==i:
            count+=1
    print(count)
    count=0
