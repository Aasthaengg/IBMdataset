n,m=map(int,input().split())

l=[list(map(int,input().split())) for i in range(m)]
from operator import itemgetter as it
l.sort(key=it(1))
head=0
ans=0
for a,b in l:
    if not(a<head<=b):ans+=1;head=b
print(ans)