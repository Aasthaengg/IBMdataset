import sys
input = sys.stdin.readline   #sys.std.readlineのほうが10倍速い
N, Q = map(int, input().split())
AB = [tuple(map(int, input().split())) for i in range(N-1)]
PX = [tuple(map(int, input().split())) for i in range(Q)]
es = [[] for _ in range(N)]  #グラフ配列

for a,b in AB:
  a -= 1
  b -= 1
  es[a].append(b)
  es[b].append(a)
ps = [0] * N   #処理配列(当該のものをプラスする)
for p,x in PX:
  ps[p-1] += x
  
#print(es)
#print(ps)

ans = [0] * N #回答配列
ans[0] = ps[0]
stack = [0]  #待ち配列
visited = [0] * N #訪れたかどうか配列、最初は0、訪れたら1
visited[0] = 1
while stack: #空であればFalse、中身が入ってればTrueを返す性質
  v = stack.pop()
  for i in es[v]:
    if visited[i]:
      continue
    visited[i] = 1
    ans[i] = ans[v] + ps[i]
    stack.append(i)
print(*ans)
