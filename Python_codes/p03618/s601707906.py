a=input()
n=len(a)
ans=n*(n-1)//2
from collections import Counter
d=Counter(list(a))
for i in d:ans-=d[i]*(d[i]-1)//2
print(ans+1)