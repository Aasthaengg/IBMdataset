n=int(input())
a=list(map(int,input().split()))

r,l=0,0
ans=0
sum_a=0

while r<n:
    if sum_a+a[r]==(sum_a^a[r]):
        sum_a+=a[r]
        r+=1
        ans+=r-l
    elif l==r:
        l+=1
        r+=1
    else:
        sum_a-=a[l]
        l+=1
print(ans)