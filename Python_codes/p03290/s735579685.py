d,g=map(int,input().split())
pc=[list(map(int,input().split())) for i in range(d)]
ans=float("inf")
tmp=0
for i in range(2**d):
    count=0
    s=0
    nokori=set(range(1,d+1))
    for k in range(d):
        if i &(1<<k):
            s+=pc[k][0]*(k+1)*100+pc[k][1]
            count+=pc[k][0]
            nokori.discard(k+1)
    if s<g:
        use=max(nokori)
        n=min(pc[use-1][0],-(-(g-s)//(use*100)))
        count+=n
        s+=n*use*100
    if s>=g:
        ans=min(ans,count)
print(ans)