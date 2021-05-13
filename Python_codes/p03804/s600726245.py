n,m=map(int,input().split())
a=[input() for _ in range(n)]
b=[input() for _ in range(m)]
b1=b[0]
res="No"
for i in range(n-m+1):
    if b1 in a[i]:
        x=a[i].index(b1)
        match=1
        for j in range(1,m):
            if a[i+j][x:x+m]!=b[j]:
                match=0
        if match:
            res="Yes"
print(res)