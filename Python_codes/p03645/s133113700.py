n,m = list(map(int,input().strip().split()))

path = [[] for i in range(n)]

for i in range(m):
  a,b = list(map(int,input().split()))
  path[a-1].append(b-1)
  path[b-1].append(a-1)

for j in path[0]:
  if n-1 in path[j]:
    print("POSSIBLE")
    exit()
print("IMPOSSIBLE")