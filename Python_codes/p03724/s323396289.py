n,m=map(int,input().split())
l=[list(map(int,input().split())) for i in range(m)]
a=[0]*n
for i in range(m):
    a[l[i][0]-1]+=1
    a[l[i][1]-1]+=1
for i in range(n):
    if a[i]%2==1:
        print('NO')
        break
else:
    print('YES')
