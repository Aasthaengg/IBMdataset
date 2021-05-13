N,M=map(int,input().split())
S=sorted([list(map(int,input().split())) for _ in range(N)], key=lambda x: x[0])

ans=0
for a,b in S:
    if M<=0: break
    x=min(M,b)
    ans+=a*x
    M-=x
print(ans)