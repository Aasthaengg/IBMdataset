n = int(input())
a = list(map(int,input().split(" ")))
ave = sum(a)/n
dist = [2**50 for i in range(n)]
for i in range(n):
  dist[i] = abs(ave-a[i])
key = dist.index(min(dist))
print(key)