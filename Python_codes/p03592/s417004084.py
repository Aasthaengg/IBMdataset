n,m,k=map(int,input().split())
k=(m*n)-(k*2)
l=[]
for i in range(m+1):
    for j in range(n+1):
        if (m-2*i)*(n-2*j)==k:
            print('Yes')
            exit()
print('No')
