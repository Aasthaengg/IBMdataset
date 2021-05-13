n,m,k=map(int,input().split())
f=False
for i in range(n+1):
    for j in range(m+1):
        if k==i*m+j*n-2*i*j:
            print('Yes')
            f=True
            break
    if f:
        break
if not f:
    print('No')
