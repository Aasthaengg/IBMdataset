from math import ceil
N,K=map(int, input().split())

A=list(map(int, input().split()))

left=1
right=10**9+1
ans=float("INF")
while True:
    mid=(left+right)//2
    now=0
    for i in range(N):
        now+=ceil(A[i]/mid)-1

    if now>K:
        if left==mid:
            break
        left=mid
    else:
        ans=min(ans, mid)
        if right==mid:
            break
        right=mid

print(ans)