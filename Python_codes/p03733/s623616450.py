N, T=map(int, input().split())
a=list(map(int, input().split()))

ans=T

for i in range(N-1):
    space=a[i+1]-a[i]
    if space>=T:
        ans+=T
    else:
        loss=T-space
        ans+=T-loss

print(ans)