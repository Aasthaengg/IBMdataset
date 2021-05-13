n,m,q=map(int,input().split())

lr=[[0]*(n+1) for i in range(n+1)]
for i in range(m):
    li,ri=map(int,input().split())
    lr[li][ri]+=1
    
for i in range(n+1):
    asum=0
    for j in range(n+1):
        asum+=lr[i][j]
        lr[i][j]=asum
            
for i in range(q):
    pi,qi=map(int,input().split())
#    pi-=1
#    qi-=1
    asum=0
    for j in range(pi,qi+1):
#        print("j:",j,"j-1",j-1,"qo:",qi,lr[j][qi]-lr[j][j-1])
        asum+=lr[j][qi]-lr[j][j-1]
    print(asum)
