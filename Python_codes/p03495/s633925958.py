from collections import Counter
n,k=map(int,input().split())
a=list(map(int,input().split()))
d=Counter(a).most_common()
ans=0
for i in range(k,len(d)):
    ans+=d[i][1]
print(ans)