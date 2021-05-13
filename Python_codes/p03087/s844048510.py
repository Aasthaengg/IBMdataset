from re import finditer
from bisect import bisect_left
from bisect import bisect_right
a,b=map(int,input().split())
c=input()
d=[]
for _ in range(b):
    n,m=map(int,input().split())
    d.append([n-1,m-1])
n=len(d)
ac1=[m.start() for m in finditer('AC', c)]
ac2=[m.end()-1 for m in finditer('AC', c)]
for i in range(n):
    index1=bisect_left(ac1,d[i][0])
    index2=bisect_right(ac2,d[i][1])
    print(index2-index1)