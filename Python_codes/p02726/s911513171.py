from itertools import combinations as cb
node = []
n,x,y = map(int, input().split())
for i in range(1, n+1):
  node.append(i)
pair = list(cb(node, 2))
dist = [0]*n
for a in pair:
  if a[1] <= x or a[0] >= y:
    dist[a[1]-a[0]] += 1
  else:
    dist[min(abs(x-a[0])+abs(y-a[1])+1,a[1]-a[0])] += 1
for i in range(1, n):
  print(dist[i])