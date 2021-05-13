N = int(input())
G = [[] for _ in range(N)]
que_f = [0]
que_s = [N-1]
dis_f = [-1]*N
dis_s = [-1]*N
for i in range(N-1):
  a, b = map(int,input().split())
  a -= 1
  b -= 1
  G[a].append(b)
  G[b].append(a)

visited_f = [False]*N
dis_f[0] = 0
while que_f:
  pos = que_f.pop(0)
  for next_pos in G[pos]:
    if visited_f[next_pos] == True:
      continue
    que_f.append(next_pos)
    visited_f[pos] = True
    dis_f[next_pos] = dis_f[pos] + 1

visited_s = [False]*N
dis_s[N-1] = 0
while que_s:
  pos = que_s.pop(0)
  for next_pos in G[pos]:
    if visited_s[next_pos] == True:
      continue
    que_s.append(next_pos)
    visited_s[pos] = True
    dis_s[next_pos] = dis_s[pos] + 1
    
f = 0
s = 0
for i in range(N):
  if dis_f[i] <= dis_s[i]:
    f += 1
  else:
    s += 1

if f >s:
  print('Fennec')
else:
  print('Snuke')