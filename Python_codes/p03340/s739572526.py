N=int(input())
a=list(map(int,input().split()))
cnt=0
r=0
sum=0
for l in range(N):
    while r<N and sum^a[r]==sum+a[r]:
        sum+=a[r]
        r+=1
        if r>=N:break
    cnt+=r-l
    if l==r:
        r+=1
    else:
        sum-=a[l]
print(cnt)
