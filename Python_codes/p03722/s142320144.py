inf=10**43
n,m=map(int,input().split())
edges=[None]*m 
for i in range(m):
    a,b,c=map(int,input().split())
    a-=1 
    b-=1 
    edges[i]=(a,b,-c)
d=[inf]*n 
f=1 
d[0]=0 
for i in range(n-1): 
    for (a,b,c) in edges: 
        if d[a]+c<d[b]:
            d[b]=d[a]+c #update distances 
#print(d)
for i in range(n):
    for (a,b,c) in edges: 
        if d[b]>d[a]+c:  #how can a->b be minimised by travelling 
                         #some other path
            if b==n-1:
                f=0
                #print(b,d[b])
            else:
                d[b]=d[a]+c 
if f:  
    print(-d[n-1])
else:
    print('inf')