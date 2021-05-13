n,m,k=map(int,input().split())

if k>n*m:
    print('No')
    exit()
    
if k%n==0 or k%m==0:
    print('Yes')
    exit()
k=min(m*n-k,k)
for i in range(1,n):
    for j in range(1,m):
        if i*m+j*n-2*i*j==k:
            print('Yes')
            exit()
print('No')