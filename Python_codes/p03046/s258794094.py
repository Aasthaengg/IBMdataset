m,k = map(int, input().split())

if( k >= 2**m):
    print(-1)
    exit()

if( (m==1) & (k==1) ):
    print(-1)
    exit()


n = 2**(m+1)
ans = [0] * n
if( k==0):
    for i in range(n):
        ans[i] = i//2
    print(' '.join([str(i) for i in ans ]))
    exit()

ans[0] = k
ind = 1
for i in range(n//2):
    if(i != k):
        ans[ind] = i
        ind += 1

ans[ind] = k
ind += 1

for i in range(n//2 -1, -1, -1):
    if(i != k):
        ans[ind] = i
        ind += 1


print(' '.join([str(i) for i in ans ]))