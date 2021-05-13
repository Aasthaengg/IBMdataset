n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(str(input())))
for i in range(m):
    if a[0][i]!='#':
        a[0][i]=1
    else:
        j=i
        while(j<m):
            a[0][j]=0
            j+=1
        break
for i in range(n):
    if a[i][0]!='#':
        a[i][0]=1
    else:
        j=i
        while(j<n):
            a[j][0]=0
            j+=1
        break
for i in range(1,n):
    for j in range(1,m):
        if a[i][j]!='#':
            a[i][j]=a[i-1][j]+a[i][j-1]
        else:
            a[i][j]=0
print(a[-1][-1]%((10**9)+7))