n=int(input())
a=list(map(int,input().split()))
from collections import Counter
c=Counter(a)
cnt=0
for b in c.values():
    cnt+=b-1

if cnt%2==0:
    print(n-cnt)
else:
    print(n-cnt-1)
