n,v,u = map(int,input().split())
dist_taka = [100000 for i in range(n)]
dist_aoki = [100000 for i in range(n)]
dist_taka[v-1] = 0
dist_aoki[u-1] = 0
M = [[] for i in range(n)]
for i in range(n-1):
  a,b = map(int,input().split())
  M[a-1].append(b-1)
  M[b-1].append(a-1)
stack = []
check = [0]*n
for i in range(len(M[v-1])):
  stack.append([v-1,M[v-1][i]])
while len(stack) != 0:
  cur = stack.pop()
  check[cur[0]] = 1
  dist_taka[cur[1]] = dist_taka[cur[0]]+1
  for i in range(len(M[cur[1]])):
    if check[M[cur[1]][i]] == 0:
      stack.append([cur[1],M[cur[1]][i]])

check = [0]*n
for i in range(len(M[u-1])):
  stack.append([u-1,M[u-1][i]])
while len(stack) != 0:
  cur = stack.pop()
  check[cur[0]] = 1
  dist_aoki[cur[1]] = dist_aoki[cur[0]]+1
  for i in range(len(M[cur[1]])):
    if check[M[cur[1]][i]] == 0:
      stack.append([cur[1],M[cur[1]][i]])
ans = 0
for i in range(n):
  if dist_taka[i] < dist_aoki[i]:
    ans = max(ans,dist_aoki[i])
print(max(0,ans-1))