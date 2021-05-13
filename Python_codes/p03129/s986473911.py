#「みんなのプロコン 2019」a
n,k=map(int,input().split())
i=1
cnt=0
while i<=n:
    cnt+=1
    i+=2

if cnt>=k:
    print('YES')
else:
    print('NO')
