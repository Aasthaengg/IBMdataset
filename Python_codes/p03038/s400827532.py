n,m=map(int,input().split())
a=sorted(map(int,input().split()))
l=list()
for i in range(m):
    l.append(list(map(int,input().split())))
l.sort(key=lambda x:-x[1])
i=0
for b,c in l:
    for j in range(b):
        if i+j<n and a[i+j]<c:
            a[i+j]=c
        else:
            print(sum(a))
            exit()
    i+=b
print(sum(a))