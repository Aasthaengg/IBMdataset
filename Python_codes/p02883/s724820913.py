from math import ceil
N,K=map(int, input().split())
A=list(map(int, input().split()))
F=list(map(int, input().split()))
A=sorted(A)
F=sorted(F, reverse=True)

left=0
right=10**12+1
ans=float("INF")
while True:
    mid=(left+right)//2

    now=0
    for i in range(N):
        if F[i]*A[i]>mid:
            now+=ceil(((F[i]*A[i])-mid)/F[i])
    #print(now, mid)
    if now==K:
        ans=min(ans, mid)
        if right==mid:
            break
        right=mid
    elif now>K:
        if left==mid:
            break
        left=mid
    else:
        if right==mid:
            break
        right=mid
        ans=min(ans, mid)

print(ans)