from collections import deque

N, M, Q = map(int, input().split())

query = [list(map(int, input().split())) for _ in range(Q)]

rlt = 0

stc = deque([])
for i in range(1,M+1):
  stc.append([0,i])

while stc:
  lst = stc.pop()
  if len(lst) == N+1:
    now = 0
    for a,b,c,d in query:
      if lst[b] - lst[a] == c:
        now += d
    rlt = max(rlt, now)
  else:
    for j in range(lst[-1],M+1):
      tmp = lst + [j]
      stc.append(tmp)

print(rlt)