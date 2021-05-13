from collections import Counter
n=int(input())
lst=list(map(int,input().split()))
c=Counter(lst)
c=c.most_common()
ans=0
for i in range(len(c)):
    if c[i][0]<c[i][1]:
        ans+=(c[i][1]-c[i][0])
    elif c[i][0]>c[i][1]:
        ans+=(c[i][1])
print(ans)