N,K = map(int,input().split())

mx = (N-1)*(N-2)//2
if K > mx:
  print(-1)
  exit()

ans = []
for i in range(N-1):
  ans.append((i+1, N))

add = mx-K
edge = []
for i in range(N-1):
  for j in range(i):
    edge.append((i+1, j+1))

for i in range(add):
  ans.append(edge[i])

print(len(ans))
for u,v in ans:
  print(u,v)