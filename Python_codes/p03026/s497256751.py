n=int(input())
ab=[list(map(int,input().split())) for _ in range(n-1)]
c=list(map(int,input().split()))
c.sort()
print(sum(c)-c[-1])
ki=[[] for _ in range(n)]
ki_ji=[[i,0] for i in range(n)]
for a,b in ab:
  a,b=a-1,b-1
  ki[a].append(b)
  ki[b].append(a)
  ki_ji[a][1]+=1
  ki_ji[b][1]+=1
# 1番大きい値の隣には2番目に大きい値を入れたい。
# 次数最大のノードを始点にしてBFS的に値を入れていく。
from collections import deque
ki_ji.sort(key=lambda x:x[1])
seen=[0]*n
t=ki_ji[-1]
todo=deque([t[0]])
seen[t[0]]=c.pop()
while todo:
  t=todo.popleft()
  l=ki[t]
  for li in l:
    if seen[li]==0:
      todo.append(li)
      seen[li]=c.pop()
print(' '.join(map(str,seen)))
#print(ki_ji)
