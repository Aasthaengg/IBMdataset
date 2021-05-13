n=int(input())
lst=[int(input()) for i in range(n)]

from collections import Counter
c=Counter(lst)
c=c.most_common()
ans=0
for i in c:
    if i[-1]%2==1:
        ans+=1
print(ans)