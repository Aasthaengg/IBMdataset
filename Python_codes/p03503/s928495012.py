n=int(input())

F=[list(map(int,input().split())) for _ in range(n)]
P=[list(map(int,input().split())) for _ in range(n)]

ans=(10**9)*(-1)
for i in range(1,2**10):
    cnt=[0]*n
    for j in range(10):
        if i>>j &1:
            for x in range(n):
                if F[x][j]==1:
                    cnt[x]+=1
    tmp=0
    for k in range(n):
        tmp+=P[k][cnt[k]]
    ans=max(ans,tmp)

print(ans)



