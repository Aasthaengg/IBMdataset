N,M=map(int,input().split())
ab=[list(map(int,input().split()))for _ in range(N)]
ab.sort()

ans=0
countM=0
for a,b in ab:
    b=min(b,M-countM)
    a*=b
    ans+=a
    countM+=b
    if countM==M:
        break

print(ans)