n = int(input())
lst = list(map(int, input().split()))
lst.append(0)
lst.insert(0, 0)

dist = []
for i in range(n+1):
  dist.append(abs(lst[i+1]-lst[i]))

sum_dist = sum(dist)
for i in range(n):
  ans = sum_dist-(dist[i]+dist[i+1])
  ans += abs(lst[i]-lst[i+2])
  print(ans)