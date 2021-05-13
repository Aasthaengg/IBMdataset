n,k=map(int,input().split())
w=[int(input()) for i in range(n)]
left=max(w)-1;right=sum(w)
mid=0
while left+1<right:
    mid=(left+right)//2
    sum=0;count=1
    for wi in w:
        if wi+sum>mid:
            sum=wi
            count+=1
        else:
            sum+=wi
    if count<=k:
        right=mid
    else:
        left=mid

print(right)
