n,k=map(int,input().split())
ans=0 
curr=0 
l=[int(i) for i in input().split()]
for i in range(39,-1,-1):
    c=0 
    for j in range(n):
        if l[j]&(1<<i):
            c+=1 
    a=c 
    b=n-c 
    if b>a:
        if curr+(1<<i)<=k:
            curr+=(1<<i)
print(sum(i^curr for i in l))