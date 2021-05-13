import heapq
n, k = map(int, input().split())
r = min(n, k)
v = list(map(int, input().split()))
ans = 0
for i in range(1, r+1):
  for j in range(i+1):
    a = j
    b = i-j
    v_temp = v[:a]
    v_temp.extend(v[n-b:])
    heapq.heapify(v_temp)
    for l in range(k-i):
      get = heapq.heappop(v_temp)
      if get>=0:
        heapq.heappush(v_temp, get)
        break
      if not v_temp:
        break
    v_temp.append(0)
    ans = max(ans, sum(v_temp))
print(ans)