n,m=map(int,input().split())
abc=[]
for i in range(m):
    a,b,c=map(int,input().split())
    abc.append([a-1,b-1,-c])
abc.sort()
INF=10**18
d=[INF]*n
chk=[False]*n
d[0]=0
for i in range(n-1):
    for a,b,c in abc:
        if d[b]>d[a]+c:
            d[b]=d[a]+c
for i in range(n):
    for a,b,c in abc:
        if d[b]>d[a]+c:
            d[b]=d[a]+c
            chk[b]=True
            chk[a]=True
if chk[n-1]==True:
    print('inf')
else:
    print(-d[n-1])