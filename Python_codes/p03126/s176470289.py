n,m=map(int,input().split())
l=[0]*(m+1)
for u in range(n):
    d=list(map(int,input().split()))
    for i in range(1,d[0]+1):
        l[d[i]]+=1
c=0
for i in range(1,m+1):
    if(l[i]==n):
        c=c+1
print(c)
