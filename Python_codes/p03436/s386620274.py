from collections import deque
H, W = map(int, input().split())
m = []
for i in range(H):
  m.append(input())
#白の個数数える(スタートゴール以外)
cnt0 = -2
for ma in m:
  for n in ma:
    if n == ".":
      cnt0 += 1
q = deque([(0,0)])
v = [[float("inf")]*W for i in range(H)]
v[0][0] = 0
g = (H-1, W-1)
move = ((0,1), (1,0), (0,-1), (-1,0))  
#ゴールの白個数はカウントしないから-1スタート
cnt1 = -1
#ここからBFS
while q:
  s = q.popleft()
  for mo in move:
    ns = (s[0]+mo[0], s[1]+mo[1])
    if 0<=ns[0]<=H-1 and 0<=ns[1]<=W-1 and v[ns[0]][ns[1]]==float("inf") and m[ns[0]][ns[1]]==".":
      q.append(ns)
      if v[ns[0]][ns[1]]>v[s[0]][s[1]]+1:
        v[ns[0]][ns[1]] = v[s[0]][s[1]]+1
    if ns == g:
      cnt1 += v[g[0]][g[1]]
      break
  if ns == g:
    break

if v[g[0]][g[1]]==float("inf"):
  print(-1)
else:
  print(cnt0-cnt1)