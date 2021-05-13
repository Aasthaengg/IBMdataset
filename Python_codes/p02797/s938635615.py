N,K,S=map(int, input().split())
ans=[0]*N
if K==0:
    if S==10**9:
        for i in range(N):
            ans[i]=S-1
    else:
        for i in range(N):
            ans[i]=S+1
else:
    for i in range(K):
        ans[i]=S
    if S==10**9:
        for i in range(K,N):
            ans[i]=S-1
    else:
        for i in range(K,N):
            ans[i]=S+1
print(*ans)