INF = 10**20
N,M = map(int,input().split())
node = [[] for _ in range(N)]
for _ in range(M):
  l,r,d = map(int,input().split())
  node[l-1].append([r-1,d])
  node[r-1].append([l-1,-1*d])
 
ans = "Yes"
pos = [INF]*N
for i in range(N):
  if pos[i]==INF:
    que = [[i,0]]
    while(que):
      c,cp = que.pop()
      if pos[c]==INF:
        pos[c] = cp
        for n,d in node[c]:
          if pos[n]==INF:
            que.append([n,cp+d])
          elif pos[n] != cp+d:
            ans="No"
            break
        else:
          continue
        break
      elif pos[c] != cp:
        ans="No"
        break
    else:
      continue
    break
print(ans)