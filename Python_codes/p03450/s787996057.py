n,m=map(int,input().split())
a=[[]for i in range(n+1)]
b=[""]*(n+1)
for i in range(m):
    l,r,d=map(int,input().split())
    a[l].append([r,d])
    a[r].append([l,-d])
for i in range(1,n+1):
    if b[i]=="":
        b[i]=0
        k=[i]
        while k:
            s=k.pop()
            for x,y in a[s]:
                if b[x]=="":
                    k.append(x)
                    b[x]=b[s]+y
c="Yes"
for i in range(1,n+1):
    for p,q in a[i]:
        if b[i]+q!=b[p]:
            c="No"
print(c)