from collections import Counter

l=[]
for i in range(3):
 a,b=map(int,input().split())
 l.append(a)
 l.append(b)

c=Counter(l)
if max(c.values())==2:
 print('YES')
else:
 print('NO')