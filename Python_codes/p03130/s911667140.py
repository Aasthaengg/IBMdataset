import collections

l=[]
for i in range(3):
  A1,A2=map(int,input().split())
  l.append(A1)
  l.append(A2)

c=collections.Counter(l).most_common()

if len(set(l))==4 and c[0][1]==2:
  print('YES')
else:
  print('NO')