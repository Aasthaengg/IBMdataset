from collections import Counter
n,k=map(int,input().split())
lst=list(map(int,input().split()))
c=Counter(lst)
c=c.most_common()
ans=0
for i in range(k,len(c)):
    ans+=c[i][1]
print(ans)