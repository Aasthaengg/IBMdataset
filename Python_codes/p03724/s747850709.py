import sys


N, M = map(int, input().split())

d = {i:0 for i in range(1, N+1)}

for i in range(M):
  a, b = map(int, input().split())
  d[a] += 1
  d[b] += 1
  
for v in d.values():
  if v % 2 == 0:
    continue
  else:
    print("NO")
    sys.exit()
    
print("YES")