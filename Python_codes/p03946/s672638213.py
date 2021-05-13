n,t=map(int,input().split())
a=list(map(int,input().split()))

mi=[a[0]]
ma=[a[n-1]]
for i in range(1,n):
    if a[i]<mi[-1]:
        mi.append(a[i])
    else:
        mi.append(mi[-1])

for i in range(n-2,-1,-1):
    if a[i]>ma[-1]:
        ma.append(a[i])
    else:
        ma.append(ma[-1])

ma.reverse()

sa=0
for i in range(n):
    x=ma[i]-mi[i]
    sa=max(sa,x)
se=set()
for i in range(n):
    if ma[i]-mi[i]==sa:
        se.add(mi[i])

print(len(se))
