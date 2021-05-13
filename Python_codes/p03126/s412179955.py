n,m=map(int,input().split())
k=[]
c=list(range(1,m+1))
for i in range(n):
    a=list(map(int,input().split()))
    a.pop(0)
    k.append(a)
for i in range(1,m+1):
    cnt=0
    for j in range(n):
        if k[j].count(i)>0:
            cnt+=1
    if cnt!=n:
        c.remove(i)
print(len(c))

    
