from collections import Counter
import itertools as it

N=int(input())
l=[]
for i in range(N):
    l.append(tuple(map(int,input().split())))
l.sort()

if N==1:
    ans=1
else:
    d=[(c[1][0]-c[0][0],c[1][1]-c[0][1]) for c in it.combinations(l,2)]
    ans=N-max(dict(Counter(d)).values())

print(ans)