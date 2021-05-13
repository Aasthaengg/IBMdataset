a=input()
n=len(a)
ans=n*(n-1)//2+1
from collections import Counter as co
for i in co(list(a)).values():
    ans-=(i*(i-1))//2
print(ans)