n=int(input())
a=list(map(int,input().split()))
sum=0
cnt=0
# 奇数+
for i in range(n):
    sum+=a[i]
    if i%2==0:
        if sum>=0:
            cnt+=(sum+1)
            sum=-1
    else:
        if sum<=0:
            cnt+=(1-sum)
            sum=1
cnt_sbst=cnt
# 奇数-
cnt=0
sum=0
for i in range(n):
    sum+=a[i]
    if i%2==1:
        if sum>=0:
            cnt+=(sum+1)
            sum=-1
    else:
        if sum<=0:
            cnt+=(1-sum)
            sum=1
cnt_plus=cnt
ans=min(cnt_plus,cnt_sbst)
print(ans)


