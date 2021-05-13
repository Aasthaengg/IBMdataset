n, m = map(int,input().split())

road=[]
for i in range(n):
  road.append([])

for i in range(m):
  a, b = map(int,input().split())
  road[a-1].append(b)
  road[b-1].append(a)
  
for i in range(n):
  print(len(road[i]))
