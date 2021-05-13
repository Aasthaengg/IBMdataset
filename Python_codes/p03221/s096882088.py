n,m=map(int,input().split())
import bisect
l=[[] for _ in range(n)]
l2=[]

for i in range(m):
  p,y=map(int,input().split())
  l[p-1].append(y)
  l2.append([p,y])

for m in l:
  m.sort()
for m in l2:
  print("{:06d}".format(m[0]) +"{:06d}".format(bisect.bisect_left(l[m[0]-1],m[1])+1))
