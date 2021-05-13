from collections import defaultdict
n=int(input())
d=defaultdict(int)
for i in range(n):
    a=int(input())
    d[a]+=1

sm=0
for i,j in d.items():
    sm+=j%2

print(sm)