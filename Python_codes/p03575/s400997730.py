# 条件下の「橋」を、「エッジを1つしか持たないノード」から
#「エッジを3つ以上持つノード」の間にあるエッジと考える
from collections import defaultdict

def remove_checked():
  global check_nodes,dd
  for n in check_nodes:
    if n in dd:
      dd.pop(n)
    for k in dd:
      if n in dd[k]:
        dd[k].remove(n)
  check_nodes=set()        

n,m=map(int,input().split())
dd=defaultdict(list)
check_nodes=set()
for i in range(m):
  a,b=map(int,input().split())
  dd[a].append(b)
  dd[b].append(a)

cnt=0
while True:
  for k in dd.keys():
    if k in check_nodes:
      continue
    nodes=dd[k]
    if len(nodes) == 1:
      nxt=k
      while len(nodes) <= 2:
        check_nodes.add(nxt)
        cnt+=1
        nxt=nodes[0]
        if nxt in check_nodes:
            nxt = nodes[1]
        nodes=dd[nxt]
        if len(nodes) == 1:
          check_nodes.add(nxt)
          break
  if check_nodes==set():
    break
  remove_checked()

print(cnt)    