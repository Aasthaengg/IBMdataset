import copy
n,m = map(int,input().split())
graph = [[] for _ in range(n*3)]
for i in range(m):
  u,v = map(int,input().split())
  for j in range(3):
    graph[n*j+u-1].append((n*(j+1)+v-1)%(3*n))
s,t = map(int,input().split())
wait = [s-1]
cnt = 0
done = [0]*(3*n)
while wait:
  cnt += 1
  now = copy.copy(wait)
  wait = []
  for i in now:
    for j in graph[i]:
      if not done[j]:
        done[j] = 1
        wait.append(j)
      if j == t-1:
        print(cnt//3)
        quit()
print(-1)