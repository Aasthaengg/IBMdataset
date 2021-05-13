from collections import deque
 
N = int(input())
As = [deque([])]
for _ in range(N):
  As.append(deque(list(map(int, input().split()))))

cnt = 0
cset = set([i for i in range(1,N+1)])
while len(cset) > 0:
  cnt += 1
  fset = set()
  nex = set([])
  f = 1
  for i in cset:
    if i not in fset:
      if As[As[i][0]][0] == i and As[i][0] not in fset:
        vis = As[i].popleft()
        fset.add(vis)
        fset.add(As[vis].popleft())
        if len(As[i]) > 0:
          nex.add(i)
        if len(As[vis]) > 0:
          nex.add(vis)
        f = 0
  cset = nex
  if f == 1:
    print('-1')
    exit()
      
print(cnt)