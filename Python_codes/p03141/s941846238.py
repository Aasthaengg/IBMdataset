n=int( input())
a=[0]*n
b=[0]*n
for i in range(n):
    a[i],b[i] = map(int,input().split() )
c=[[a[i],b[i],a[i]+b[i]] for i in range(n)]
c.sort(reverse=True,key=lambda x:x[2])
tsum=sum(c[i*2][0] for i in range((n+1)//2))
asum=sum(c[i*2+1][1] for i in range(n//2))
print( tsum- asum )