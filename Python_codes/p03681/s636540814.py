N,M=map(int,input().split())
perm=1
ans=0
perm2=1
if N==M:

    for i in range(N):
        perm=(perm*(i+1))%((10**9)+7)
    ans=(perm*perm*2)%((10**9)+7)

elif abs(N-M)==1:
    for i in range(N):
        perm=(perm*(i+1))%((10**9)+7)
    for i in range(M):
        perm2=(perm2*(i+1))%((10**9)+7)
    
    ans=(perm*perm2)%((10**9)+7)

else:
    ans=0

print(ans)