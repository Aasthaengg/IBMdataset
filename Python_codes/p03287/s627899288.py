n,m=map(int,input().split())
from collections import  Counter
from itertools import accumulate
a=list(map(int,input().split()))
b=list(accumulate(a))
b=[0]+b
b=list(map(lambda x:x%m ,b))
e=Counter(b)
ans=0
for i in e.values():
    ans+=i*(i-1)//2

print(ans)