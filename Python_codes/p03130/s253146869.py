a=[[int(i) for i in input().split()] for i in range(3)]
import collections 
d=collections.defaultdict(int)
for i in a:
    d[i[0]]+=1
    d[i[1]]+=1
x=[]
for i in d.values():
    x.append(i)
if x.count(1)==2 and x.count(2)==2:
    print("YES")
else:
    print("NO")