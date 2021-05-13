n,m=map(int,input().split())
from collections import defaultdict
d=defaultdict(int)

for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    d[a]+=1
    d[b]+=1

for i in range(n):
    if d[i]%2==1:
        print('NO')
        exit()
print('YES')