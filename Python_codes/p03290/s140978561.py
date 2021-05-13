d,g=list(map(int,input().split()))
p=[list(map(int,input().split()))for i in range(d)]

ans=float("inf")
for bit in range(1<<d):
    count=0;
    sum=0;
    nokori=set(range(1,d+1))
    for i in range(d):
        if bit&(1<<i):
            sum+=p[i][0]*(i+1)*100+p[i][1]
            count+=p[i][0]
            nokori.discard(i+1)
    if sum>=g:
        ans=min(ans,count)
    else:
        use=max(nokori)
        n=min(p[use-1][0],-(-(g-sum)//(100*use)))
        count+=n
        sum+=n*use*100
        if sum>=g:
            ans=min(ans,count)
print(ans)