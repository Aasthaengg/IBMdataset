import math
n=int(input())
a=list(map(int,input().split()))
cnt=0
ans=0
for i in range(n-1):
    if a[i]==a[i+1]:
        cnt+=1
    else:
        cnt+=1
        if 1<cnt:
            ans+=math.floor(cnt/2)
            cnt=0
        else:
            cnt=0
if a[-2]==a[-1]:
    cnt+=1
    ans+=math.floor(cnt/2)

print(ans)