n,m,k = map(int,input().split())
nya = False
for i in range(n+1):
    for j in range(m+1):
        if i*m + j*n - 2*i*j == k:
            nya = True
            break
if nya:
    print('Yes')
else:
    print('No')
