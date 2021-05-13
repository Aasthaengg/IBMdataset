from collections import Counter
n=int(input())
c=Counter(input())
ans=1
for i in c.most_common():
 ans*=(i[1]+1)
 ans%=10**9+7
print((ans-1)%(10**9+7))