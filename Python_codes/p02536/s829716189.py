def nxto(u):
  for val in m[u]:
    if c[val] == 0:
      return val
    
  return None

def dfs(ix):
  stk = [ix]
  c[ix] = 1
  while stk != []:
    l = stk[-1]
    nxt = nxto(l)
    if nxt is not None:
      c[nxt] = 1
      stk.append(nxt)
    else:
      stk.pop()

N, M = list(map(int, input().split(" ")))
c = [0 for _ in range(N+1)]
m = [[] for _ in range(N+1)]
for _ in range(M):
  a, b = list(map(int, input().split(" ")))
  m[a].append(b)
  m[b].append(a)

cnt = -1
for i in range(1, N+1):
  if c[i] == 0:
    dfs(i)
    cnt += 1
print(cnt)