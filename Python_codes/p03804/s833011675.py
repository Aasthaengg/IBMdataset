n,m=map(int,input().split())
a=list()
b=list()
for i in range(n):
    a.append(list(input()))
for i in range(m):
    b.append(list(input()))

for g in range(n-m+1):
    for h in range(n-m+1):
        p=0
        for i in range(m):
            p+=a[g+i][h:h+m]==b[i]
        if p==m:
            print('Yes')
            exit()
print('No')