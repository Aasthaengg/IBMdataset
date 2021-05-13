n,m,k=map(int, input().split())
count=0

for i in range(n+1):
    for j in range(1,m+1):
        count=(i*m)+(j*n)-2*(i*j)
        if count==k:
            print('Yes')
            exit()

print('No')