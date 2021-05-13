n, k = map(int, input().split())

p = list(map(int, input().split()))

for i in range(1, len(p)):
  p[i] += p[i-1]
ans = p[k-1]
for i in range(k, n):
  ans = max(ans, p[i]-p[i-k])

print((k+ans)/2)