n,m=map(int,input().split())
*h,=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(m)]
b=[1]*n
for i in range(m):
    if h[a[i][0]-1] > h[a[i][1]-1]:
        b[a[i][1]-1]*=0
    elif h[a[i][0]-1] < h[a[i][1]-1]:
        b[a[i][0]-1]*=0
    else:
        b[a[i][0]-1]*=0
        b[a[i][1]-1]*=0
#    print(b)
print(b.count(1))