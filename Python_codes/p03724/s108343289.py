N,M=map(int,input().split())
cnt=[0]*N
for i in range(M):
    a,b=map(lambda x:int(x)-1,input().split())
    if a>b:
        a,b=b,a
    if a==0:
        cnt[b]+=1
    else:
        cnt[a]+=1
        cnt[b]+=1
for i in range(1,N):
    if cnt[i]%2:
        print('NO')
        exit()
print('YES')