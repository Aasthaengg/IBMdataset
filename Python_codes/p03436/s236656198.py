import sys
from collections import deque
readline=sys.stdin.readline
read=sys.stdin.read

h,w=map(int,readline().split())
wb={'#':0,'.':1}
s=[wb[g] for g in read() if g!='\n']
dist=[0]*(h*w)
dist[0]=1
stack=deque([(0,0)])
while stack:
  cg=stack.popleft()
  for i in range(4):
    ng=(cg[0]+(1-2*(i&1))*(i>>1),cg[1]+(1-2*(i&1))*(1-(i>>1)))
    fcg=w*cg[0]+cg[1]
    fng=w*ng[0]+ng[1]
    if 0<=ng[0]<=h-1 and 0<=ng[1]<=w-1 and \
        s[fng] and dist[fng]==0:
      stack.append(ng)
      dist[fng]=dist[fcg]+1
if dist[-1]:
  print(sum(s)-dist[-1])
else:
  print(-1)
