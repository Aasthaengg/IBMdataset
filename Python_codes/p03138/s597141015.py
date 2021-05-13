n,k=map(int,input().split())
A=list(map(int,input().split()))
if k==0:
    print(sum(A))
    exit()
ans=sum(A)
for i in range(40,-1,-1):
    if 2**i > k:
        continue
    cnt=0
    for a in A:
        if 1<<i & a:
            cnt+=1
    if cnt<n-cnt:
        k-=2**i
        ans -=cnt*2**i
        ans += (n-cnt)*2**i

print(ans)
