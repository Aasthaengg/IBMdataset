from collections import Counter

n,k=map(int,input().split())
l=[int(i) for i in input().split()]
c=Counter(l).most_common()
if len(c)<=k:
    ans=0
else:
    sum=0
    for i in range(0,k):
        sum+=c[i][1]
        ans=n-sum

print(ans)
