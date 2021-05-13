X, Y, Z, K = map(int, input().split())
x = sorted(list(map(int, input().split())))
y = sorted(list(map(int, input().split())))
z = sorted(list(map(int, input().split())))


import heapq
ans = []
for i in range(X-1, -1, -1):
  for j in range(Y-1, -1, -1):
    for k in range(Z-1, -1, -1):
      if (X-i)*(Y-j)*(Z-k) <= K:
        sub = x[i]+y[j]+z[k]
        ans.append(sub)
      else:
        break
ans = list(map(lambda x: x*(-1), ans)) 
heapq.heapify(ans)
for i in range(K):
  print(heapq.heappop(ans)*(-1))