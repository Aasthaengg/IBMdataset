N=int(input())
A=[int(i) for i in input().split()]
prev=-1
ans=0
cnt=1
for a in A:
    if prev==a:
        cnt+=1
    else:
        ans+=cnt//2
        cnt=1
    prev=a
ans+=cnt//2
print(ans)