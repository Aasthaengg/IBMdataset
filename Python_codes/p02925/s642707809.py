from collections import deque
 
N = int(input())
As = [[]]
iset = [0]*(N+1)
for _ in range(N):
  As.append(list(map(int, input().split())))

cnt = 0
cset = set([i for i in range(1,N+1)])
while len(cset) > 0:
  cnt += 1
  fset = set()
  nex = set()
  f = 1
  for i in cset:
    if i not in fset:
      vis = As[i][iset[i]]
      if As[vis][iset[vis]] == i and vis not in fset:
        iset[i] += 1
        iset[vis] += 1
        fset.add(i)
        fset.add(vis)
        if iset[i] < N-1:
          nex.add(i)
        if iset[vis] < N-1:
          nex.add(vis)
        f = 0
  cset = nex
  if f == 1:
    print('-1')
    exit()
    
print(cnt)