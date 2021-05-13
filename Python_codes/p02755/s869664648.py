a,b=map(int,input().split())
from math import floor
ans=-1

q=[]
for i in range(1,20000):
    if a==floor(i*0.08) and b==floor(i*0.1):
        q.append(i)

if q:
    print(min(q))
else:
    print(ans)
