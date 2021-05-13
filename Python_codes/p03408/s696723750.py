from collections import defaultdict as ddf
n=int(input())
s=[input() for _ in range(n)]
m=int(input())
t=[input() for _ in range(m)]

dd=ddf(lambda:0)
for e in s: dd[e]+=1
for e in t: dd[e]-=1
print(max(0,max(dd.values())))