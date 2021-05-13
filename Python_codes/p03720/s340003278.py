n,m=map(int,input().split())
result=[]
count=[]
for i in range(n):
    result.append(i+1)
    count.append(0)
for i in range(m):
    a,b=map(int,input().split())
    count[result.index(a)]+=1
    count[result.index(b)]+=1
for i in range(n):
    print(count[i])