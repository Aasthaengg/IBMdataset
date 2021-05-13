from collections import defaultdict
n=int(input())
c=[]
for _ in range(n): c.append(list(map(int,input().split())))
dic=defaultdict(int)
for i in range(n):
    for j in range(n):
        if i==j: continue
        dic[(c[i][0]-c[j][0],c[i][1]-c[j][1])]+=1
if dict(dic): print(n-max(dic.values()))
else: print(1)