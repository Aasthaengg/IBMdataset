n=int(input())
from itertools import groupby as gb
ans=0
for a,b in gb(list(map(int,input().split()))):
    ans+=len(list(b)) //2
print(ans)