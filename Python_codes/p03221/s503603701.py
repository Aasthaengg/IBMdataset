import bisect
N, M = map(int, input().split())
l_1 = [[] for i in range(N+1)]
l_2 = []
for i in range(M):
  p, y = map(int, input().split())
  l_1[p].append(y)
  l_2.append([p, y])
  
for i in range(N+1):
  l_1[i].sort()
    
for i in range(M):
  c = l_2[i]
  n = bisect.bisect_left(l_1[c[0]], c[1]) + 1
  ans = str(c[0]).zfill(6) + str(n).zfill(6)
  print(ans)
