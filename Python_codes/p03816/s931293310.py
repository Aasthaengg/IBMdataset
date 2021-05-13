from collections import Counter
n=int(input())
lst=list(map(int,input().split()))
c=Counter(lst)
lst=list(c.values())
ans=0
tmp=0
for i in lst:
    if i%2==1:
        ans+=1
    else:
        tmp+=1
if tmp%2==0:
    ans+=tmp
else:
    ans+=tmp-1
print(ans)