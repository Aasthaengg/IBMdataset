n,m=map(int,input().split())
che=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    che[a-1] += 1
    che[b-1] += 1
    
error=0
for i in range(n):
    if che[i]%2!=0:
        error += 1

if error==0:
    print('YES')
else:
    print('NO')