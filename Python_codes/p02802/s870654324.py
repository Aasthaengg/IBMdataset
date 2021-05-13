n,m=map(int,input().split())
a=[0]*n
wa=0
for i in range(m):
    p,s=input().split()
    p=int(p)
    if s=="WA" and a[p-1]!=1:
        a[p-1]-=1
    elif s=="AC" and a[p-1]!=1:
        wa-=a[p-1]
        a[p-1]=1

print(a.count(1),wa)